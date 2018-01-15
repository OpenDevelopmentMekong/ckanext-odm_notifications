import os
import sys
import json
from nose.tools import assert_equal, assert_in, with_setup
import logging
import unittest
from unittest.case import SkipTest
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))
import mock
import sys

sys.modules['pylons'] = mock.MagicMock()
sys.modules['ckan'] = mock.MagicMock()
sys.modules['ckan.plugins'] = mock.MagicMock()
sys.modules['ckan.model'] = mock.MagicMock()
sys.modules['ckan.logic'] = mock.MagicMock()
sys.modules['ckan.plugins.toolkit'] = mock.MagicMock()
sys.modules['genshi'] = mock.MagicMock()
sys.modules['ckan.lib'] = mock.MagicMock()
sys.modules['ckan.lib.navl'] = mock.MagicMock()
sys.modules['ckan.lib.navl.dictization_functions'] = mock.MagicMock()

import odm_notifications_helper
log = logging.getLogger(__name__)

class TestHelpers(unittest.TestCase):

	@classmethod
	def setup_class(self):
		"set up test fixtures"

	@classmethod
	def teardown_class(self):
		"tear down test fixtures"

	def test_dummy(self):
		assert True
