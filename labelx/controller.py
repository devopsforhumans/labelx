#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module handles the API calls"""

# Import builtin python libraries
import json
import logging
import sys

# Import external python libraries
import click
import requests

# Import custom (local) python packages
from .api_manager import call_api_endpoint, get_headers
from .settings import generate_endpoints, accepted_status_codes, generate_payload
from .utils import goodbye

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


def labelx_controller(
    endpoint=None,
    project_id=None,
    group_id=None,
    custom_config_path=None,
    custom_labels_path=None,
    custom_badges_path=None,
):
    """
    Label creation controller function

    :param endpoint: (str) labels/badges endpoint
    :param project_id: (int) Numeric project number
    :param group_id: (int) Numeric group number
    :param custom_config_path: (str) custom config path
    :param custom_labels_path: (str) Custom label information .yaml file path
    :param custom_badges_path: (str) Custom badge information .yaml file path
    :returns: (stdout) Output on screen
    """

    skipped = []
    api_method = "POST"
    endpoint_url, host = generate_endpoints(
        endpoint_type=endpoint, project_id=project_id, group_id=group_id
    )
    headers = get_headers()
    all_data = generate_payload(endpoint_type=endpoint, scm_host=host, custom_data_file_path=None)
    for data_key, data_value in all_data.items():
        data_value["name"] = data_key
        try:
            payload = json.dumps(data_value, indent=4)
        except TypeError:
            click.secho(
                f"[x] TypeError detected!. Skipping [{data_key}].....", fg="red"
            )
            skipped.append(data_key)
            payload = None
        if payload:
            click.secho(f"[$] Creating {endpoint[:-1]} - ", fg="cyan", nl=False)
            click.secho(f"[{data_key}]", fg="white", nl=False)
            click.secho(f" ..... ", fg="yellow", nl=False)
            logging.debug(f"Payload: {payload}")
            api_response = call_api_endpoint(
                method=api_method,
                api_url=endpoint_url,
                data=payload,
                api_headers=headers,
            )
            if api_response.status_code in accepted_status_codes:
                click.secho(f"DONE", fg="green")
            else:
                click.secho(f"FAILED ({api_response.reason})", fg="red")
                skipped.append(data_key)
        else:
            skipped.append(data_key)
    goodbye(before=True, data=skipped)
