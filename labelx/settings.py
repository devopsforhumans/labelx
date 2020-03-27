#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Setting parameters module for labelx"""

# Import builtin libraries
import json
import logging
import os
import sys

# Import external python libraries
import click
import yaml

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar.hossain@global.ntt"

# Setting parameters
api_version = "v4"
accepted_status_codes = [200, 201, 202]
max_col_length = 88
default_protocol = "https"
default_hostname = "gitlab.com"


# Read configurations
def _read_yaml(yaml_file_path=None):
    """
    This private method reads configurations from a .yml file

    :param yaml_file_path: Configuration files full path (default and custom)
    """
    logging.debug(f"[$] Reading yaml file.....")
    with open(yaml_file_path, "r") as stream:
        try:
            defaults = yaml.load(stream, Loader=yaml.FullLoader)
        except Exception as err:
            click.secho(f"ERROR: {err}", fg="red")
            sys.exit(1)
    return defaults


# Generate payloads
def generate_labels(label_file_path=None):
    """
    Parse file or default values to generate a list of labels with attributes

    :param label_file_path: (str) Full Path to Labels (YAML) file
    :returns: (dict) key value pair of the label name and attributes
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    labels_yaml_file = os.path.join(dir_path, "labels.yaml")
    defaults = _read_yaml(yaml_file_path=labels_yaml_file)
    logging.debug(f"[$] Defaults (before custom): {defaults}")
    if label_file_path:
        custom_labels = _read_yaml(yaml_file_path=label_file_path)
        for c_label in custom_labels.keys():
            defaults[c_label] = custom_labels[c_label]
        logging.debug(f"[$] Defaults (after custom): {defaults}")
    return defaults


# Generate Endpoints
def generate_endpoints(project_id=None):
    """
    Get API endpoints

    :param project_id: (str) GitLab Project ID
    :returns: (str) API endpoint
    """

    if isinstance(project_id, int):
        all_configs = False
        if not all_configs:
            protocol = default_protocol
            host = default_hostname
        else:
            protocol = "blah"
            host = "blah"
        endpoint = f"{protocol}://{host}/api/{api_version}/projects/{project_id}/labels"
        return endpoint

    else:
        click.secho(f"[x] No project ID found! Provide project ID!", fg="red")
        return False

