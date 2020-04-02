#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import builtin libraries
import os
import shutil
from pathlib import Path
import unittest

# Import external python libraries
import yaml

# Import custom (local) python libraries
from labelx.settings import generate_labels, generate_endpoints, read_yaml
from labelx import __package_name__ as package_name


class TestSettings(unittest.TestCase):
    """
    Test settings class
    """

    def setUp(self, custom_dir=None):
        self.test_file_dir = Path(__file__).parent.absolute()
        self.test_file_path = self.test_file_dir / "test.yaml"
        self.fake_test_file_path = self.test_file_dir / "fake.yaml"
        self.txt_test_file_path = self.test_file_dir / "test_text_file.txt"
        self.txt_string = """This is a text file
        This should return error as yaml loader can not read this file
        """
        self.config_dict = {
            "login": {"host": "test.gitlab.com", "protocol": "https", "token": "secret"}
        }
        if custom_dir is None:
            self.base_dir = Path(Path.home()) / f".config/"
        else:
            self.base_dir = Path(custom_dir)
        self.config_dir = Path(f"{package_name}")
        self.config_file = "config.yaml"
        self.config_path = self.base_dir / self.config_dir / self.config_file

    def tearDown(self):
        if self.txt_test_file_path.exists():
            os.remove(self.txt_test_file_path)
        if self.config_path.parent.exists():
            shutil.rmtree(self.config_path.parent)

    # Create TEXT file
    def _create_txt_file(self):
        try:
            with open(self.txt_test_file_path, "w") as txt_stream:
                txt_stream.write(self.txt_string)
        except Exception as err:
            print(f"Error: {err}")

    # Create TMP config file
    def _create_tmp_config(self):
        if not self.config_path.exists():
            os.makedirs(self.config_path.parent)
        try:
            with open(self.config_path, "w") as yaml_stream:
                yaml.dump(self.config_dict, yaml_stream)
        except yaml.YAMLError as err:
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

    def test_settings_endpoint_returns_system_exit_if_project_id_not_provided(self):
        self.assertRaises(SystemExit, generate_endpoints)

    def test_settings_endpoint_returns_a_string(self):
        TestSettings._create_tmp_config(self)
        self.assertIsInstance(generate_endpoints(project_id=1234), str)

    def test_settings_endpoint_returns_correct_project_id(self):
        TestSettings._create_tmp_config(self)
        self.assertEqual(
            generate_endpoints(project_id=1234),
            "https://test.gitlab.com/api/v4/projects/1234/labels",
        )

    def test_settings_endpoint_returns_system_exit_with_non_integer_project_id(self):
        self.assertRaises(
            SystemExit, generate_endpoints, "this_will_raises_system_exit"
        )

    def test_settings_endpoint_returns_correct_protocol_and_host(self):
        custom_dir_path = str(Path.home())
        TestSettings.setUp(self, custom_dir=custom_dir_path)
        TestSettings._create_tmp_config(self)
        self.assertEqual(
            generate_endpoints(project_id=1234, custom_config_path=self.config_path),
            "https://test.gitlab.com/api/v4/projects/1234/labels",
        )


if __name__ == "__main__":
    unittest.main(buffer=True)
