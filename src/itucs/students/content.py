from plone.dexterity.content import Item


class EnrollmentRequest(Item):

    def __init__(self, *args, **kwargs):
        super(EnrollmentRequest, self).__init__(*args, **kwargs)
