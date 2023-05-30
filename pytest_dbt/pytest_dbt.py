import json
from typing import Dict, List, Set, Optional, Any

from pytest import Config
from sqlglot import executor
from sqlglot.executor.table import Table
import pandas as pd

from pytest_dbt.dbt_context import DbtContextSingleton, DBTModelDetails
import os


def pytest_addoption(parser):
    parser.addini(
        name="dbt_manifest_file_path",
        help="DBT manifest file path",
        type="string",
    )


def execute_query(model: DBTModelDetails, tables: Optional[Dict]) -> Table:
    return executor.execute(sql=model.compiled_code, tables=tables)


def get_upstream_models(refs: List[Dict[str, str]]) -> Set[str]:
    return set([v['name'] for v in refs])


def assert_file_exists(file_path: str) -> None:
    assert os.path.isfile(file_path), "File does not exist at path: " + file_path


def get_model_details(manifest_file: str) -> Dict[str, DBTModelDetails]:
    assert_file_exists(manifest_file)
    with open(manifest_file) as f:
        manifest = json.load(f)
    # TODO: use the crc to make sure we are running on the new sql code file, way to make sure that manifest is compiled
    try:
        nodes = manifest['nodes']
        model_details = {}
        for k, model in nodes.items():
            if model['resource_type'] == 'model':
                model_details[model['alias']] = DBTModelDetails(
                    name=model['name'],
                    alias=model['alias'],
                    original_file_path=model['original_file_path'],
                    compiled_path=model['compiled_path'],
                    compiled_code=model['compiled_code'],
                    upstream_models=get_upstream_models(model['refs'])
                )
        return model_details
    except Exception as e:
        raise Exception("Manifest file not readable, please retry after running run `dbt compile`", e)


def pytest_configure(config: Config):
    dbt_manifest_file_path = config.getini('dbt_manifest_file_path')
    # check if the value is provided and is not empty
    if not dbt_manifest_file_path:
        raise ValueError("'dbt_manifest_file_path' is missing from pytest ini config!")
    dbt_context = DbtContextSingleton.getInstance()
    dbt_context.dbt_manifest_file_path = dbt_manifest_file_path


def table_to_dataframe(table: Table) -> pd.DataFrame:
    """
    Converts a dbt Table object to a Pandas DataFrame.

    Args:
        table (Table): The dbt Table object to convert.

    Returns:
        pd.DataFrame: A Pandas DataFrame with the same columns and rows as the dbt Table.
    """
    columns = table.columns
    rows = table.rows
    data_dict = {columns[i]: [row[i] for row in rows] for i in range(len(columns))}
    return pd.DataFrame(data_dict)


def run_model(model_name: str, tables: Dict) -> pd.DataFrame:
    """
    Args:
        model_name: name of the model to run
        tables: dictionary of tables to run the model with, keys are table names and values are dictionaries of column names and values
    """
    dbt_context = DbtContextSingleton.getInstance()
    model_details: dict[str, DBTModelDetails] = get_model_details(dbt_context.dbt_manifest_file_path)
    assert model_name in model_details, f"Model `{model_name}` not found in manifest file"
    assert tables.keys() == model_details[
        model_name].upstream_models, f"Model {model_name} requires {model_details[model_name].upstream_models} found {set(tables.keys())}"
    print(f"Running model {model_name} with tables {tables}")
    model_results = execute_query(model_details[model_name], tables)
    return table_to_dataframe(model_results)
