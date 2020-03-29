#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import builtin libraries
import os
from pathlib import Path
import unittest

# Import custom (local) python libraries
from labelx.settings import generate_labels, generate_endpoints, read_yaml


class TestSettings(unittest.TestCase):
    """
    Test settings class
    """

    def setUp(self):
        self.test_file_dir = Path(__file__).parent.absolute()
        self.test_file_path = self.test_file_dir / "test.yaml"
        self.fake_test_file_path = self.test_file_dir / "fake.yaml"
        self.txt_test_file_path = self.test_file_dir / "test_text_file.txt"
        self.txt_string = """This is a text file
        This should return error as yaml loader can not read this file
        """

    def tearDown(self):
        if self.txt_test_file_path.exists():
            os.remove(self.txt_test_file_path)

    # Create TEXT file
    def _create_txt_file(self):
        try:
            with open(self.txt_test_file_path, "w") as txt_stream:
                txt_stream.write(self.txt_string)
        except Exception as err:
            print(f"Error: {err}")

    # read_yaml()

    def test_settings_read_yaml_function_works_standalone(self):
        self.assertIsInstance(read_yaml(yaml_file_path=self.test_file_path), dict)

    def test_settings_read_yaml_standalone_returns_error_if_file_not_found(self):
        self.assertRaises(FileNotFoundError, read_yaml, self.fake_test_file_path)

    def test_settings_read_yaml_returns_false_if_file_is_not_yaml(self):
        TestSettings._create_txt_file(self)
        self.assertFalse(read_yaml(yaml_file_path=self.txt_test_file_path))

    # generate_labels()

    def test_settings_reads_yaml_files(self):
        self.assertIsInstance(generate_labels(), dict)

    def test_settings_returned_yaml_list_size(self):
        self.assertGreater(len(generate_labels()), 0)

    def test_settings_read_custom_file(self):
        self.assertIsInstance(
            generate_labels(label_file_path=self.test_file_path), dict
        )

    def test_settings_raises_error_if_custom_file_is_not_found(self):
        self.assertRaises(FileNotFoundError, generate_labels, self.fake_test_file_path)

    # generate_endpoints()

    def test_settings_endpoint_returns_false_if_project_id_not_provided(self):
        self.assertFalse(generate_endpoints())

    def test_settings_endpoint_returns_a_string(self):
        self.assertIsInstance(generate_endpoints(project_id=1234), str)

    def test_settings_endpoint_returns_correct_project_id(self):
        self.assertEqual(
            generate_endpoints(project_id=1234),
            "https://gitlab.com/api/v4/projects/1234/labels",
        )

    def test_settings_endpoint_returns_false_with_non_integer_project_id(self):
        self.assertFalse(generate_endpoints(project_id="this_will_raise_type_error"))


if __name__ == "__main__":
    unittest.main(buffer=True)
