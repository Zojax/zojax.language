##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface, i18n
from zope.component import getUtility
from zope.i18n.negotiator import Negotiator

from interfaces import ISiteLanguage


class SiteLanguage(Negotiator):
    interface.implements(ISiteLanguage)

    def getLanguage(self, langs, request):
        if self.usebrowser:
            if langs is None:
                langs = [self.language]
            return super(SiteLanguage, self).getLanguage(langs, request)
        else:
            return self.language


def negotiate(context):
    return getUtility(ISiteLanguage).getLanguage(
        i18n.ALLOWED_LANGUAGES, context)


i18n.negotiate = negotiate
