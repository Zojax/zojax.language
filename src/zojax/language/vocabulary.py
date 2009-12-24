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
import os
from zope.i18n import translate, locales
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

locale = locales.locales.getLocale('en')

languages = {}
for key, value in locale.displayNames.languages.items():
    if key.lower()==key and len(key)==2:
        languages[key] = value

territories = {}
for key, value in locale.displayNames.territories.items():
    if key.upper()==key and len(key)==2:
        territories[key] = value

terms = []
for name in os.listdir(os.path.join(os.path.dirname(locales.__file__), 'data')):
    name = name[:-4]

    if len(name) == 2 and name in languages:
        title = u'%s [%s]'%(languages[name], name)
    elif len(name) == 5:
        lang, terr = name.split('_')
        name = u'%s-%s'%(lang, terr)
        if lang not in languages:
            continue
        title = u'%s/%s [%s]'%(languages[lang], territories[terr], name.lower())
    else:
        continue

    terms.append((title, SimpleTerm(name, str(name), title)))


terms.sort()
LanguagesVocabulary = SimpleVocabulary([term for title, term in terms])
