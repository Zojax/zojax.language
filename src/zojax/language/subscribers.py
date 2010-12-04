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
from zope import component
from zope.component import getUtility
from zope.app.component.interfaces import ISite
from zope.app.publication.interfaces import IBeforeTraverseEvent
from zope.i18n.interfaces import IModifiableUserPreferredLanguages

from interfaces import ISiteLanguage


@component.adapter(ISite, IBeforeTraverseEvent)
def languageSelector(context, event):
    configlet = getUtility(ISiteLanguage)
    languages = IModifiableUserPreferredLanguages(event.request, None)
    if languages is not None:
        if not configlet.usebrowser:
            languages.setPreferredLanguages([configlet.language])
        else:
            del languages._getLanguagesData()['overridden']
            del languages._getLanguagesData()['cached']
        event.request.setupLocale()