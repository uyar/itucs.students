# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s itucs.students -t test_enrollment_request.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src itucs.students.testing.ITUCS_STUDENTS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_enrollment_request.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Enrollment_Request
  Given a logged-in site administrator
    and an add enrollment_request form
   When I type 'My Enrollment_Request' into the title field
    and I submit the form
   Then a enrollment_request with the title 'My Enrollment_Request' has been created

Scenario: As a site administrator I can view a Enrollment_Request
  Given a logged-in site administrator
    and a enrollment_request 'My Enrollment_Request'
   When I go to the enrollment_request view
   Then I can see the enrollment_request title 'My Enrollment_Request'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add enrollment_request form
  Go To  ${PLONE_URL}/++add++Enrollment_Request

a enrollment_request 'My Enrollment_Request'
  Create content  type=Enrollment_Request  id=my-enrollment_request  title=My Enrollment_Request


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the enrollment_request view
  Go To  ${PLONE_URL}/my-enrollment_request
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a enrollment_request with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the enrollment_request title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
