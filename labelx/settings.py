#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Setting parameters module for labelx"""

# Import builtin libraries
import logging
import os
import sys

# Import external python libraries
import click
import yaml

# Import custom (local) python packages
from . import config_manager

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"

# Setting parameters
api_version = "v4"
accepted_status_codes = [200, 201, 202]
max_col_length = 88
allowed_extensions = ["yaml", "yml"]


# Default link url modification for badges endpoint
def mod_defaults(init_dict=None, host=None):
    """
    This method adds the host name before all required link_url

    :param init_dict: (dict) a python dictionary that needs modification
    :param host: (str) Source code management host url
    :retuns:
    """

    ret_dict = {}
    for data_key, data_value in init_dict.items():
        if "%" in data_value["link_url"]:
            data_value["link_url"] = f"{host}/{data_value['link_url']}"
            ret_dict[data_key] = data_value
        else:
            ret_dict[data_key] = data_value
    logging.debug(f"Modified defaults: {ret_dict}")
    return ret_dict


# Read configurations
def read_yaml(yaml_file_path=None):
    """
    This method reads configurations from a .yaml file

    :param yaml_file_path: Configuration files full path (default and custom)
    :returns: (dict) a python dictionary with yaml file data
    """

    logging.debug(f"[$] Reading yaml file.....")
    file_ext = str(yaml_file_path).rsplit(".", 1)[1]
    if file_ext in allowed_extensions:
        with open(yaml_file_path, "r") as stream:
            try:
                defaults = yaml.load(stream, Loader=yaml.FullLoader)
            except Exception as err:
                click.secho(f"[x] ERROR: {err}", fg="red")
                sys.exit(1)
        return defaults
    else:
        return False


# Generate payloads
def generate_payload(endpoint_type=None, scm_host=None, custom_data_file_path=None):
    """
    Parse file or default values to generate a list of labels with attributes

    :param endpoint_type: (str) labels/badges endpoint string
    :param scm_host: (str) Source code management host url
    :param custom_data_file_path: (str) Full Path to Labels (YAML) file
    :returns: (dict) key value pairs of the label name and attributes
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_file = f"{endpoint_type}.yaml"
    data_yaml_file = os.path.join(dir_path, data_file)
    defaults = read_yaml(yaml_file_path=data_yaml_file)
    logging.debug(f"[$] Defaults (before custom): {defaults}")
    if endpoint_type == "badges":
        default_data = mod_defaults(init_dict=defaults, host=scm_host)
    else:
        default_data = defaults
    if custom_data_file_path:
        custom_data = read_yaml(yaml_file_path=custom_data_file_path)
        for c_name, c_value in custom_data.items():
            default_data[c_name] = c_value
        logging.debug(f"[$] Default data (after custom): {default_data}")
    return default_data


# Generate Endpoints
def generate_endpoints(
    endpoint_type=None, project_id=None, group_id=None, custom_config_path=None
):
    """
    Get API endpoints

    :param endpoint_type: (str) labels/badges?
    :param project_id: (int) GitLab Project ID
    :param group_id: (int) GitLab Group ID
    :param custom_config_path: (str) Configuration file path
    :returns: (str) API endpoint
    """

    if custom_config_path:
        all_configs = config_manager.load_config(config_file_paths=[custom_config_path])
    else:
        all_configs = config_manager.load_config()
    protocol = all_configs["login"]["protocol"]
    host = all_configs["login"]["host"]
    host_url = f"{protocol}://{host}"
    if isinstance(project_id, int):
        endpoint = f"{host_url}/api/{api_version}/projects/{project_id}/{endpoint_type}"
    elif isinstance(group_id, int):
        endpoint = f"{host_url}/api/{api_version}/groups/{group_id}/{endpoint_type}"
    else:
        click.secho(f"[x] No project ID/Group ID found!", fg="red")
        sys.exit(1)
    logging.debug(f"Endpoint: {endpoint}")
    return [endpoint, host_url]


# Define authentication
def get_authentication():
    """
    Generates the authentication

    :return: (str/tuple) Authentication
    """

    configs = config_manager.load_config()
    if configs:
        login = configs["login"]
    else:
        sys.exit(1)

    token = login["token"]
    logging.debug(f"Authentication Token: {token}")
    return token
