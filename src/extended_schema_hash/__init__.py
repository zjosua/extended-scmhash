# Extended Schema Hash for Anki
#
# Copyright (C) 2018-2020  zjosua <https://github.com/zjosua>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

ES_DEV = False

from anki.hooks import wrap
from anki.models import ModelManager
from anki.utils import checksum

if ES_DEV:
    from aqt import mw
    from aqt.utils import showText
    from aqt.qt import *

def extscmhash(self, m, _old):
    "Return a hash of parts of the schema, to check model compatibility."
    _old(self, m)

    s = m['css']
    for f in m['flds']:
        s += f['name']
    for t in m['tmpls']:
        s += t['name']
        for fmt in ('qfmt', 'afmt'):
            s += t[fmt]
    return checksum(s)

ModelManager.scmhash = wrap(ModelManager.scmhash, extscmhash, "around")

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

if ES_DEV:
    action = QAction("anki-extended-scmhash &Debug", mw)
    action.triggered.connect(debug)
    mw.form.menuTools.addAction(action)
