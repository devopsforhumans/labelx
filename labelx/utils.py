#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Utility module for labelx"""

# Import builtin python libraries
import logging
import sys

# Import external python libraries
import click

# Import custom (local) python packages
from . import __license__ as package_license
from . import __package_name__ as package_name
from . import __version__ as version
from . import __author__ as author
from . import __author_email as author_email
from . import __copyright__ as copy_right
from . import settings

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


# Divider function
def divider(text="", char="-"):
    """
    Print a divider with a headline:

    :param text: (unicode) Headline text. If empty, only the line is printed.
    :param char: (unicode) Line character to repeat, e.g. =.
    :return: (stdout) on screen
    """

    pretty = True
    line_max = settings.max_col_length
    if len(char) != 1:
        raise ValueError(
            "Divider chars need to be one character long. " "Received: {}".format(char)
        )
    if pretty:
        deco = char * (int(round((line_max - len(text))) / 2) - 2)
        text = " {} ".format(text) if text else ""
        text = f"{deco}{text}{deco}"
    if len(text) < line_max:
        text = text + char * (line_max - len(text))
    click.secho(text, fg="magenta")


# Initial message
def initial_message():
    """This function shows the initialization message"""

    click.secho(f"[*] Initializing.....", fg="cyan")
    click.secho(
        f"[*] Please use 'labelx --help' to see all available options", fg="cyan"
    )
    divider(f"[{package_name}]")


# Banner
def banner():
    """This function show a banner"""

    banner_string = f"""
+--------------------------------------------------+
|                     {package_name}                       |
+--------------------------------------------------+
| about: GitLab label/badge creator                |
| author: {author} ({author_email})          |
| version: {version}                                   |
| license: {package_license}           |
| documentation: https://labelx.readthedocs.io/    |
+--------------------------------------------------+
"""
    click.secho(f"{banner_string}", fg="green")


# Goodbye
def goodbye(before=False, data=None):
    """
    Shows goodbye message

    :param before: (boolean) Whether to show a message before goodbye
    :param data: (dict) skipped information
    :return: (stdout) On screen output
    """

    if before:
        if data:
            divider("Before we leave, Please note ")
            click.secho(f"[*] Total skipped: {len(data)}", fg="cyan")
            click.secho(f"[*] Skipped : ", fg="cyan", nl=False)
            click.secho(f"{data}", fg="yellow")
        divider("Goodbye!")
    else:
        divider("Goodbye!")


# Turn on/off debugging
def debug_manager():
    """This function acts accordingly with --debug switch"""

    try:
        from http.client import HTTPConnection
    except ImportError:
        click.secho(f"[x] Can't import http client", fg="red")
        sys.exit(1)
    click.secho(f"[+] ", nl=False, fg="yellow")
    click.secho(f"DEBUG mode is ON", fg="black", bg="yellow")
    debug_format = click.style(
        "[+] %(levelname)s %(asctime)-15s [%(filename)s:%(lineno)s - %(funcName)20s() ]"
        " %(message)s",
        fg="yellow",
    )
    HTTPConnection.debuglevel = 4
    logging.basicConfig(format=debug_format)
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


# Show only package info
def _show_author_info():
    """This private function shows author information"""

    divider("Author Information")
    author_info = {
        "Package Name": package_name,
        "Version": version,
        "Author": author,
        "Contact": author_email,
        "License": package_license,
        "Copyright": copy_right,
    }
    for key, value in author_info.items():
        click.secho(f"[*] {key}: ", fg="cyan", nl=False)
        click.secho(f"{value}", fg="yellow")


# Show only package info
def _show_pkg_info():
    """This private function shows package information"""

    divider("Package Information")
    pkg_info = {
        "Package Name": package_name,
        "Version": version,
        "License": package_license,
    }
    for key, value in pkg_info.items():
        click.secho(f"[*] {key}: ", fg="cyan", nl=False)
        click.secho(f"{value}", fg="yellow")


# Show information about the package
def show_info(view_type=None):
    """
    This function prints information about the package on screen

    :param view_type: (boolean) To show more or less info
    :returns: (stdout) output to the screen
    """

    if view_type == "all":
        _show_pkg_info()
    if view_type == "author":
        _show_author_info()
    goodbye()


# Validate file extension
def validate_file_extension(ctx, param, value):
    """This function validates file extensions"""

    if value:
        try:
            ext = value.rsplit(".", 1)[1]
        except AttributeError:
            return False
        if ext not in settings.allowed_extensions:
            click.secho(
                f"[x] Provided file extension [{ext}] is not allowed!", fg="red"
            )
            click.secho(
                f"[!] Use {settings.allowed_extensions} file extensions!", fg="blue"
            )
            ctx.abort()
        else:
            return value
