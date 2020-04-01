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
from .settings import generate_endpoints, accepted_status_codes, generate_labels
from .utils import goodbye

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@protonmail.com"


def create_label_controller(
    project_id=None, custom_config_path=None, custom_labels_path=None
):
    """
    Label creation controller function

    :param project_id: (int) Numeric project number
    :param custom_config_path: (str) custom config path
    :param custom_labels_path: (str) Custom label information yaml path
    :returns: (stdout) Output on screen
    """

    all_labels = generate_labels()
    skipped_labels = []
    api_method = "POST"
    endpoint_url = generate_endpoints(project_id=project_id)
    headers = get_headers()
    for label_key, label_value in all_labels.items():
        label_value["name"] = label_key
        try:
            payload = json.dumps(label_value, indent=4)
        except TypeError:
            click.secho(
                f"[x] TypeError detected!. Skipping [{label_key}].....", fg="red"
            )
            skipped_labels.append(label_key)
            payload = None
        if payload:
            click.secho(f"[$] Creating label - [{label_key}].....", fg="blue", nl=False)
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
                skipped_labels.append(label_key)
        else:
            skipped_labels.append(label_key)
    goodbye(before=True, data=skipped_labels)
