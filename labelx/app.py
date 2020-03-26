#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module for labelx"""

# Import builtin python libraries
import logging
import sys

# Import external python libraries
import click

# Import custom (local) python libraries
from .utils import debug_manager, initial_message, show_info, validate_file_extension

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@protonmail.com"


# Alias group class
class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        matched_commands = ", ".join(sorted(matches))
        print(matched_commands)
        ctx.fail(f"Too many matches: {matched_commands}")


# Click context manager class
class Context(object):
    """Click context manager class"""

    def __init__(self):
        """Constructor method for click context manager class"""

        self.debug = False
        self.initial_msg = False


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group(cls=AliasedGroup)
@click.option(
    "--debug",
    "debug",
    is_flag=True,
    default=False,
    show_default=True,
    help="Turns on DEBUG mode.",
    type=str,
)
@click.version_option()
@pass_context
def mission_control(context, debug):
    """Rancher automation control panel"""

    context.debug = debug
    context.initial_msg = True
    context.dry_run = True
    context.show_help = False


@mission_control.command(short_help="Shows package information.")
@click.option(
    "--author",
    "author",
    is_flag=True,
    default=False,
    show_default=True,
    help="Shows author information.",
    type=str,
    hidden=True,
)
@pass_context
# Information about this package
def pkg_info(context, author):
    """Prints information about the package"""

    if author:
        show_info(view_type="author")
    else:
        show_info(view_type="all")
