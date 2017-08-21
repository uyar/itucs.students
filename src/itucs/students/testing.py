# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import itucs.students


class ItucsStudentsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=itucs.students)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'itucs.students:default')


ITUCS_STUDENTS_FIXTURE = ItucsStudentsLayer()


ITUCS_STUDENTS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ITUCS_STUDENTS_FIXTURE,),
    name='ItucsStudentsLayer:IntegrationTesting'
)


ITUCS_STUDENTS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ITUCS_STUDENTS_FIXTURE,),
    name='ItucsStudentsLayer:FunctionalTesting'
)


ITUCS_STUDENTS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ITUCS_STUDENTS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ItucsStudentsLayer:AcceptanceTesting'
)
