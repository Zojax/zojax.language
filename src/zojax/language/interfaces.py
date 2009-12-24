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
from zope import interface, schema
from zope.i18n.interfaces import INegotiator
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zojax.language')

import vocabulary


class ISiteLanguage(INegotiator):
    """ site language configlet """

    usebrowser = schema.Bool(
        title = _('Use browser setting'),
        default = False,
        required = True)

    language = schema.Choice(
        title = _(u'Language'),
        description = _(u'Default site language.'),
        vocabulary = vocabulary.LanguagesVocabulary,
        default = u'en',
        required = True)
