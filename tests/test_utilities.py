# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest
import os
from data_quality import utilities
import datapackage

class TestUtilities(unittest.TestCase):

    def test_that_config_is_correctly_loaded(self):
        config_filepath = os.path.join('tests', 'fixtures', 'dq.json')
        config = utilities.load_json_config(config_filepath)
        self.assertTrue(os.path.isabs(config['data_dir']))

    def test_default_datapackage_loaded(self):
        datapackage = utilities.get_default_datapackage()
        self.assertGreater(len(datapackage.resources), 0)

