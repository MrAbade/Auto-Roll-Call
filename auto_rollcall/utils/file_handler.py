from os import walk
from importlib import import_module
from re import match, sub
from typing import Callable, Generator, Iterable, List

from flask import Flask


def get_valid_modules_from_a_dir(
    app_name: str, file_pattern_regex: str
) -> List[str]:
    config_dir = f"{app_name}/configurations"
    _, _, file_list = next(walk(config_dir))
    return [
        f'{app_name}.configurations.{sub(".py", "", file)}'
        for file in file_list
        if match(file_pattern_regex, file)
    ]


def get_each_module_importation(
    module_import_name_list: Iterable[str],
) -> Generator[Callable[[Flask], None], None, None]:
    return (import_module(module) for module in module_import_name_list)


def put_database_as_first_module(
    module_import_name_list: Iterable[str],
) -> List[str]:
    return sorted(
        module_import_name_list, key=lambda value: "database" not in value
    )


def call_each_init_app_function(app: Flask, file_pattern_regex: str):
    module_list = get_valid_modules_from_a_dir(app.name, file_pattern_regex)
    normalized_module_list = put_database_as_first_module(module_list)
    for imported_module in get_each_module_importation(normalized_module_list):
        imported_module.init_app(app)
