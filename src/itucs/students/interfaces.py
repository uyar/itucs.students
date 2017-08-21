# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from itucs.students import _
from plone.supermodel import model
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IItucsStudentsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IEnrollment_Request(model.Schema):
    """Schema for Enrollment Request content type."""

    model.load('models/enrollment_request.xml')
