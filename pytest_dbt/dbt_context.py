# Singleton class
from dataclasses import dataclass
from typing import List, Set


class DbtContextSingleton:
    _instance = None
    _dbt_manifest_file_path = ""

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DbtContextSingleton._instance is None:
            DbtContextSingleton()
        return DbtContextSingleton._instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbtContextSingleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DbtContextSingleton._instance = self

    @property
    def dbt_manifest_file_path(self):
        return self._dbt_manifest_file_path

    @dbt_manifest_file_path.setter
    def dbt_manifest_file_path(self, value):
        self._dbt_manifest_file_path = value


@dataclass(frozen=True)
class DBTModelDetails:
    name: str
    alias: str
    original_file_path: str
    compiled_path: str
    upstream_models: Set[str]
    udfs: Set[str]
    compiled_code: str