#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import builtin libraries
from contextlib import contextmanager
import unittest
from io import StringIO
import sys

# Import custom (local) python libraries
from labelx.utils import initial_message, banner


class TestUtils(unittest.TestCase):
    """
    Test utils class
    """

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def test_utils_initial_message_prints_a_message(self):
        with TestUtils.captured_output(self) as (out, err):
            initial_message()
        output = out.getvalue().strip().split("\n")
        self.assertEqual(output[0], "[*] Initializing.....")

    def test_utils_banner_returns_a_message(self):
        with TestUtils.captured_output(self) as (out, err):
            banner()
        output = out.getvalue().strip().split("\n")
        matching_string = "+-"
        if matching_string in output[0]:
            message = True
        else:
            message = False
        self.assertTrue(message, True)
