#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Configuration handler module"""

# Import builtin python libraries
import logging
import os
from pathlib import Path
import sys

# Import external python libraries
import click

# Import custom (local) python packages
from . import __package_name__ as package_name
from . import settings

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


# Config and template path
home_dir = Path(Path.home())
base_locations = [
    home_dir / f".config/{package_name}",
    os.path.join(os.getcwd(), f"{package_name}"),
    f"/etc/{package_name}",
]
config_locations = [base_path for base_path in base_locations]
base_file_names = ["config"]
base_file_extensions = ["yaml", "yml"]
file_names = [
    file_name + "." + file_extension
    for file_name in base_file_names
    for file_extension in base_file_extensions
]
config_files = [
    os.path.join(config_location, file_name)
    for config_location in config_locations
    for file_name in file_names
]


# Check file permissions
def _check_file_permissions(file_paths=None):
    """
    Checks file permissions

    :param file_paths: (list) A list of paths for configuration lookup
    :returns: (boolean, boolean, str) file flag, permission flag and default config path
    """

    # Config finder flag
    file_flag = 0
    permission_flag = 0
    default_config = ""
    for path in file_paths:
        logging.debug(f"[*] Searching configs in: [{path}].....")
        if os.path.exists(path) and os.path.isfile(path):
            file_flag = 1
            if os.access(path, os.F_OK) and os.access(path, os.R_OK):
                logging.debug(f"[#] Using configs from: [{path}]")
                default_config = path
                permission_flag = 1
                break
            else:
                click.secho(f"[x] Permission ERROR: [{path}]", fg="red")
                permission_flag = 0
        else:
            file_flag = 0
    return file_flag, permission_flag, default_config


def load_config(config_file_paths=None):
    """
    This function reads and load the configurations into the system

    :param config_file_paths: (list) A list of paths for configuration lookup
    :return: (dict) Merged configurations
    """

    if config_file_paths is None:
        config_file_paths = config_files
    logging.debug(f"Default lookup paths: {config_files}")
    file_flag, permission_flag, default_config = _check_file_permissions(
        file_paths=config_file_paths
    )
    logging.debug(f"File Flag: {file_flag}")
    logging.debug(f"Permission Flag: {permission_flag}")
    logging.debug(f"Default Config: {default_config}")
    if file_flag == 1 and permission_flag == 1:
        all_configs = settings.read_yaml(yaml_file_path=default_config)
        base_directory = Path(default_config).parent
        all_configs["common"] = {}
        all_configs["common"]["base_directory"] = base_directory
        logging.debug(f"[#] Configuration read complete!")
        logging.debug(f"Configs: {all_configs}")
        return all_configs
    else:
        click.secho(f"[x] Could not locate configuration file!", fg="red")
        sys.exit(1)
