# -*- coding: utf-8 -*-
# Extended scmhash
# Copyright: Josua Zbinden - https://github.com/zjosua
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

AES_DEV = False

from anki.models import ModelManager
from anki.utils import checksum

if AES_DEV:
    from aqt import mw
    from aqt.utils import showText
    from aqt.qt import *

def extscmhash(self, m):
    "Return a hash of parts of the schema, to check model compatibility."
    s = str(m['css'])
    for f in m['flds']:
        s += f['name']
    for t in m['tmpls']:
        s += t['name']
        for fmt in ('qfmt', 'afmt'):
            s += t[fmt]
    return checksum(s)

ModelManager.scmhash = extscmhash

# Stuff used during development
##########################################################################

def debug():
    card = mw.col.sched.getCard()
    #showText(str(card.nid), title="anki-extended-scmhash debug output")
    
    note = card.note()
    #showText(str(note.model), title="anki-extended-scmhash debug output")
    
    model = note.model()
    
    # debugtext = str(model['tmpls'][0]['name'])
    # debugtext = str(model['css'])
    debugtext = str(model['name']) + str(model['tmpls'][0]['name']) \
        + ", qfmt:\n" + str(model['tmpls'][0]['qfmt'])
    # showText(debugtext, title="anki-extended-scmhash debug output")
    
    s = str(model['css'])
    for f in model['flds']:
        s += f['name']
    for t in model['tmpls']:
        s += t['name']
        for fmt in ('qfmt', 'afmt'):
            s += t[fmt]
    showText(s, title="anki-extended-scmhash debug output")
    
    # consoletext = ""
    # t = model['tmpls'][0]
    # for fmt in ('qfmt', 'afmt'):
        # consoletext += t[fmt] + "\n"
    # print(consoletext)

if AES_DEV:
    action = QAction("anki-extended-scmhash &Debug", mw)
    action.triggered.connect(debug)
    mw.form.menuTools.addAction(action)
