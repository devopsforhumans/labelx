#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module for labelx"""

# Import builtin python libraries
import logging
import sys

# Import external python libraries
import click

# Import custom (local) python libraries
from .controller import labelx_controller
from .utils import debug_manager, banner, initial_message, show_info

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


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
        self.banner = False


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
    """GitLab label creator control panel"""

    context.debug = debug
    context.initial_msg = True
    context.banner = True
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


@mission_control.command(short_help="Create labels for issues and merge requests.")
@click.option(
    "-p",
    "--project-id",
    "project_id",
    required=False,
    help="Numeric project ID.",
    type=int,
)
@click.option(
    "-g",
    "--group-id",
    "group_id",
    required=False,
    help="Numeric group ID.",
    type=int,
)
@click.option(
    "--debug",
    "sub_debug",
    is_flag=True,
    default=False,
    show_default=True,
    help="Turns on DEBUG mode.",
    type=str,
)
@pass_context
def create_labels(context, project_id, group_id, sub_debug):
    """
    Create labels in a GitLab project
    """

    if context.banner:
        banner()
    if context.debug or sub_debug:
        debug_manager()
    if context.initial_msg:
        initial_message()
    if project_id and group_id:
        click.secho(
            f"[x] Project ID and Group ID can not be used at the same time.", fg="red"
        )
        sys.exit(1)
    if all(v is None for v in [project_id, group_id]):
        click.secho(f"[x] Either Project ID or Group ID is required.", fg="red")
        sys.exit(1)
    if project_id or group_id:
        logging.debug(f"[$] Project ID: {project_id}")
        logging.debug(f"[$] Group ID: {group_id}")
        labelx_controller(
            endpoint="labels",
            project_id=project_id,
            group_id=group_id,
            custom_config_path=None,
        )


@mission_control.command(short_help="Create badges for project.")
@click.option(
    "-p",
    "--project-id",
    "project_id",
    required=False,
    help="Numeric project ID.",
    type=int,
)
@click.option(
    "-g",
    "--group-id",
    "group_id",
    required=False,
    help="Numeric group ID.",
    type=int,
)
@click.option(
    "--debug",
    "sub_debug",
    is_flag=True,
    default=False,
    show_default=True,
    help="Turns on DEBUG mode.",
    type=str,
)
@pass_context
def create_badges(context, project_id, group_id, sub_debug):
    """
    Create badges in a GitLab project
    """

    if context.banner:
        banner()
    if context.debug or sub_debug:
        debug_manager()
    if context.initial_msg:
        initial_message()
    if project_id and group_id:
        click.secho(
            f"[x] Project ID and Group ID can not be used at the same time.", fg="red"
        )
        sys.exit(1)
    if all(v is None for v in [project_id, group_id]):
        click.secho(f"[x] Either Project ID or Group ID is required.", fg="red")
        sys.exit(1)
    if project_id or group_id:
        logging.debug(f"[$] Project ID: {project_id}")
        logging.debug(f"[$] Group ID: {group_id}")
        labelx_controller(
            endpoint="badges",
            project_id=project_id,
            group_id=group_id,
            custom_config_path=None,
        )
