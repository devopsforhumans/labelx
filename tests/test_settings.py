#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import builtin libraries
import unittest

# Import custom (local) python libraries
from labelx.settings import generate_labels, generate_endpoints


class TestSettings(unittest.TestCase):
    """
    Test settings class
    """

    # generate_labels()

    def test_settings_reads_yaml_files(self):
        self.assertIsInstance(generate_labels(), dict)

    def test_settings_returned_yaml_list_size(self):
        self.assertGreater(len(generate_labels()), 0)

    def test_settings_read_custom_file(self):
        self.assertIsInstance(generate_labels(label_file_path="test.yaml"), dict)

    def test_settings_raises_error_if_custom_file_is_not_found(self):
        self.assertRaises(FileNotFoundError, generate_labels, "fake.yaml")

    # generate_endpoints()

    def test_settings_endpoint_returns_false_if_project_id_not_provided(self):
        self.assertFalse(generate_endpoints())

    def test_settings_endpoint_returns_a_string(self):
        self.assertIsInstance(generate_endpoints(project_id=1234), str)

    def test_settings_endpoint_returns_correct_project_id(self):
        self.assertEqual(generate_endpoints(project_id=1234), "https://gitlab.com/api/v4/projects/1234/labels")

    def test_settings_endpoint_returns_false_with_non_integer_project_id(self):
        self.assertFalse(generate_endpoints(project_id="this_will_raise_type_error"))


if __name__ == "__main__":
    unittest.main(buffer=True)
