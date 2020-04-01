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
__email__ = "dalwar23@protonmail.com"

# Setting parameters
api_version = "v4"
accepted_status_codes = [200, 201, 202]
max_col_length = 88
allowed_extensions = ["yaml", "yml"]


# Read configurations
def read_yaml(yaml_file_path=None):
    """
    This private method reads configurations from a .yml file

    :param yaml_file_path: Configuration files full path (default and custom)
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
def generate_labels(label_file_path=None):
    """
    Parse file or default values to generate a list of labels with attributes

    :param label_file_path: (str) Full Path to Labels (YAML) file
    :returns: (dict) key value pair of the label name and attributes
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    labels_yaml_file = os.path.join(dir_path, "labels.yaml")
    defaults = read_yaml(yaml_file_path=labels_yaml_file)
    logging.debug(f"[$] Defaults (before custom): {defaults}")
    if label_file_path:
        custom_labels = read_yaml(yaml_file_path=label_file_path)
        for c_label in custom_labels.keys():
            defaults[c_label] = custom_labels[c_label]
        logging.debug(f"[$] Defaults (after custom): {defaults}")
    return defaults


# Generate Endpoints
def generate_endpoints(project_id=None, custom_config_path=None):
    """
    Get API endpoints

    :param project_id: (int) GitLab Project ID
    :param custom_config_path: (str) Configuration file path
    :returns: (str) API endpoint
    """

    if isinstance(project_id, int):
        if custom_config_path:
            all_configs = config_manager.load_config(
                config_file_paths=[custom_config_path]
            )
        else:
            all_configs = config_manager.load_config()
        protocol = all_configs["login"]["protocol"]
        host = all_configs["login"]["host"]
        endpoint = f"{protocol}://{host}/api/{api_version}/projects/{project_id}/labels"
        logging.debug(f"Endpoint: {endpoint}")
        return endpoint
    else:
        click.secho(f"[x] No project ID found! Provide project ID!", fg="red")
        sys.exit(1)


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
