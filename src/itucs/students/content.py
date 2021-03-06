from Products.Five import BrowserView
from plone import api
from plone.dexterity.content import Item


class EnrollmentRequest(Item):

    __ac_local_roles_block__ = True

    def __init__(self, *args, **kwargs):
        super(EnrollmentRequest, self).__init__(*args, **kwargs)
        user = api.user.get_current()
        self.manage_setLocalRoles(user.id, ['Reader', 'Editor'])
        self.manage_setLocalRoles('bb-idari-ogrenci-isleri', ['Reader', 'Reviewer'])

    def csv(self):
        return u",".join(u'"' + s + u'"' for s in [
            self.student_no or u'',
            self.full_name or u'',
            self.faculty or u'',
            self.department or u'',
            self.department_other or u'',
            self.phone or u'',
            self.e_mail or u'',
            str(self.submission_date) or u'',
            (self.course_prefix + self.course_no) or u'',
            self.course_title or u'',
            self.week_slot or u'',
            self.alternative or u'',
            self.explanation or u''
        ])

def updateTitle(enrollment_request, event):
    student_no = enrollment_request.student_no
    course_prefix = enrollment_request.course_prefix
    course_no = enrollment_request.course_no
    title = u"%s - %s%s" % (student_no, course_prefix, course_no)
    enrollment_request.title = title
    enrollment_request.setTitle(title)


class EnrollmentRequestView(BrowserView):
    """Default view for an enrollment request."""


class EnrollmentRequestPrintableView(BrowserView):
    """Printable view for an enrollment request."""
