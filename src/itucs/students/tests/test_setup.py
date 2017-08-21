# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from itucs.students.testing import ITUCS_STUDENTS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that itucs.students is properly installed."""

    layer = ITUCS_STUDENTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if itucs.students is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'itucs.students'))

    def test_browserlayer(self):
        """Test that IItucsStudentsLayer is registered."""
        from itucs.students.interfaces import (
            IItucsStudentsLayer)
        from plone.browserlayer import utils
        self.assertIn(IItucsStudentsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ITUCS_STUDENTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['itucs.students'])

    def test_product_uninstalled(self):
        """Test if itucs.students is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'itucs.students'))

    def test_browserlayer_removed(self):
        """Test that IItucsStudentsLayer is removed."""
        from itucs.students.interfaces import \
            IItucsStudentsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IItucsStudentsLayer, utils.registered_layers())
