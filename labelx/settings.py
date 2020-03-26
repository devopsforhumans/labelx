#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Setting parameters module for labelx"""

# Import builtin libraries
import json
import os
import sys

# Import external python libraries
import click

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar.hossain@global.ntt"

# Setting parameters
api_version = "v3"
accepted_status_codes = [200, 201, 202]
max_col_length = 88
