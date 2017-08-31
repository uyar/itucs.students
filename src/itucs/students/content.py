from plone.dexterity.content import Item


class EnrollmentRequest(Item):

    __ac_local_roles_block__ = True


def updateTitle(enrollment_request, event):
    student_no = enrollment_request.student_no
    course_prefix = enrollment_request.course_prefix
    course_no = enrollment_request.course_no
    title = u"%s - %s%s" % (student_no, course_prefix, course_no)
    enrollment_request.title = title
    enrollment_request.setTitle(title)
