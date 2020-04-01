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
from labelx.config_manager import load_config
from labelx import __package_name__ as package_name


class TestConfigManager(unittest.TestCase):
    """Test config manager class"""

    def setUp(self, custom_dir=None):
        if custom_dir is None:
            self.base_dir = Path(Path.home()) / f".config/"
        else:
            self.base_dir = Path(custom_dir)
        self.config_dir = Path(f"{package_name}")
        self.config_file = "config.yaml"
        self.config_path = self.base_dir / self.config_dir / self.config_file
        self.config_dict = {
            "login": {"host": "gitlab.com", "protocol": "https", "token": "secret"}
        }

    def tearDown(self):
        if self.config_path.parent.exists():
            shutil.rmtree(self.config_path.parent)

    # Create TMP config file
    def _create_tmp_config(self):
        if not self.config_path.exists():
            os.makedirs(self.config_path.parent)
        try:
            with open(self.config_path, "w") as yaml_stream:
                yaml.dump(self.config_dict, yaml_stream)
        except yaml.YAMLError as err:
            print(f"Error: {err}")

    # load_config

    def test_config_manager_returns_system_exit_with_no_configs_provided(self):
        self.assertRaises(SystemExit, load_config)

    def test_config_manager_returns_a_dict_if_config_in_home_dir(self):
        TestConfigManager._create_tmp_config(self)
        self.assertIsInstance(load_config(), dict)

    def test_config_manager_returns_a_dict_if_custom_config_dir_provided(self):
        custom_config_dir = str(Path.home())
        TestConfigManager.setUp(self, custom_dir=custom_config_dir)
        TestConfigManager._create_tmp_config(self)
        self.assertIsInstance(load_config(config_file_paths=[self.config_path]), dict)

    def test_config_manager_returns_correct_base_dir_when_no_config_provided(self):
        TestConfigManager._create_tmp_config(self)
        all_configs = load_config()
        base_dir = all_configs["common"]["base_directory"]
        self.assertEqual(base_dir, self.config_path.parent)

    def test_config_manager_returns_correct_base_dir_when_custom_config_provided(self):
        custom_config_dir = str(Path.home())
        TestConfigManager.setUp(self, custom_dir=custom_config_dir)
        TestConfigManager._create_tmp_config(self)
        all_configs = load_config(config_file_paths=[self.config_path])
        base_dir = all_configs["common"]["base_directory"]
        self.assertEqual(base_dir, self.config_path.parent)
