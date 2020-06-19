#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Top-level package for labelx"""

# Import builtin python libraries
import logging
from logging import NullHandler
import warnings

# Import external python libraries
from urllib3.exceptions import DependencyWarning, InsecureRequestWarning
from urllib3.exceptions import SNIMissingWarning

# urllib3's DependencyWarnings, InsecureRequestWarning should be silenced.
warnings.simplefilter("ignore", DependencyWarning)
warnings.simplefilter("ignore", InsecureRequestWarning)

# urllib3 sets SNIMissingWarning to only go off once,
# while this test suite requires it to always fire
# so that it occurs during test_requests.test_https_warnings
warnings.simplefilter("always", SNIMissingWarning)

# Set default logging handler to avoid "No handler found" warnings
logging.getLogger(__name__).addHandler(NullHandler())
