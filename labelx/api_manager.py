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
from .settings import generate_endpoints, get_authentication

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


# Define get headers function
def get_headers():
    """
    This function returns appropriate headers

    :return: (dict) A python dictionary of headers
    """

    authentication_token = get_authentication()
    headers = {
        "PRIVATE-TOKEN": authentication_token,
        "Content-Type": "application/json",
    }
    logging.debug(f"[*] API Headers: {headers}")
    return headers


# Define get api endpoint
def get_api_endpoint(pid=None, config_path=None):
    """
    Generates api endpoint for api call

    :param pid: (int) Project ID
    :param config_path: (str) Custom configuration path
    :return: (str) Full API endpoint
    """

    api_end_point = generate_endpoints(project_id=pid, custom_config_path=config_path)
    logging.debug(f"[*] API endpoint: {api_end_point}")
    return api_end_point


# Define a method to make the api call
def call_api_endpoint(
    method=None,
    api_url=None,
    data=None,
    api_headers=None,
    parameters=None,
    api_auth=None,
):
    """
    This module makes the API call

    :param method: (str) API call method e.g. GET, POST etc
    :param api_url: (str) API endpoint
    :param data: (str) API call payload body [should be JSON/XML]
    :param api_headers: (dict) API headers to be appended to the call
    :param parameters: (dict) Querystring for the API call
    :param api_auth: (base64) Authentication string
    :returns: (response) Python requests response
    """

    if data is None:
        json_input = None
    else:
        json_input = data
    logging.debug(f"Payload (call_api_endpoint): {json_input}")
    logging.debug(f"[*] Making API call.....")
    try:
        response = requests.request(
            method,
            api_url,
            data=json_input,
            headers=api_headers,
            auth=api_auth,
            params=parameters,
            verify=False,
        )
    except Exception as err:
        click.secho(f"[x] ERROR: {err}", fg="red")
        sys.exit(1)
    else:
        return response
