from importlib import import_module
from os import walk
from re import match, sub
from typing import Callable, Generator, Iterable, List, Union

from flask import Flask


def get_valid_modules_from_a_dir(
    app_name: str,
    path_to_config: str,
    file_pattern_regex: str,
) -> List[str]:
    config_dir = f"{app_name}/{path_to_config.replace('.', '/')}"
    _, _, file_list = next(walk(config_dir))
    return [
        f'{app_name}.{path_to_config}.{sub(".py", "", file)}'
        for file in file_list
        if match(file_pattern_regex, file)
    ]


def get_each_module_importation(
    module_import_name_list: Iterable[str],
) -> Generator[Callable[[Flask], None], None, None]:
    return (import_module(module) for module in module_import_name_list)


def orgainze_priority_on_sequence(
    module_import_name_list: Iterable[str],
    priority_module_list: List[str],
) -> List[str]:
    return sorted(
        module_import_name_list,
        key=lambda value: any(
            priority_module not in value
            for priority_module in priority_module_list
        ),
    )


def call_each_init_app_function(
    app: Flask,
    path_to_config: str,
    priority_module_list: Union[List[str], None],
    file_pattern_regex: str,
):
    module_list = get_valid_modules_from_a_dir(
        app.name,
        path_to_config,
        file_pattern_regex,
    )
    if priority_module_list:
        normalized_module_list = orgainze_priority_on_sequence(
            module_list,
            priority_module_list,
        )
    for imported_module in get_each_module_importation(normalized_module_list):
        imported_module.init_app(app)
