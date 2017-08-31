# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from itucs.students.interfaces import IEnrollmentRequest
from itucs.students.testing import ITUCS_STUDENTS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class Enrollment_RequestIntegrationTest(unittest.TestCase):

    layer = ITUCS_STUDENTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Enrollment_Request')
        schema = fti.lookupSchema()
        self.assertEqual(IEnrollmentRequest, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Enrollment_Request')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Enrollment_Request')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IEnrollmentRequest.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Enrollment_Request',
            id='Enrollment_Request',
        )
        self.assertTrue(IEnrollmentRequest.providedBy(obj))
