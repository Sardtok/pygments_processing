# Processing for Pygments is a Pygments lexer and style for Processing.  
# Copyright (C) 2015  Sigmund Hansen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pygments.lexer import bygroups, inherit
from pygments.lexers.jvm import JavaLexer
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Text

class ProcessingLexer(JavaLexer):
    """
    An extension to the JavaLexer that has more fine-grained token types
    for Processing specific extensions.
    """
    name = 'Processing'
    aliases = ['processing', 'pde']
    filenames = ['*.pde']
    tokens = {'root': [(r'#[A-Fa-f0-9]{6}', Number.Color), inherit]}
              
    PROCESSING_BUILTINS = [
        'draw',
        'setup',
        'mouseButton',
        'mouseClicked',
        'mouseDragged',
        'mousePressed',
        'mouseReleased',
        'mouseWheel',
        'mouseX',
        'mouseY',
        'pmouseX',
        'pmouseY',
        'key',
        'keyCode',
        'keyPressed',
        'keReleased',
        'keyTyped',
    ]

    PROCESSING_TYPES = [
        'Array',
        'ArrayList',
        'FloatDict',
        'FloatList',
        'HashMap',
        'IntDict',
        'IntList',
        'JSONArray',
        'JSONObject',
        'Object',
        'String',
        'StringDict',
        'StringList',
        'Table',
        'TableRow',
        'XML',
        'BufferedReader',
        'color',
        'PShape',
        'PrintWriter'
        'PImage',
        'PGraphics',
        'PShader',
        'PFont',
        'PVector',
    ]

    PROCESSING_CONSTANTS = [
        'HALF_PI',
        'PI',
        'QUARTER_PI',
        'TAU',
        'TWO_PI ',
    ]
    
    PROCESSING_LIBRARY = [
        'background',
        'clear'
        'colorMode',
        'fill',
        'noFill',
        'noStroke',
        'stroke',
        'size',
    ]

    def get_tokens_unprocessed(self, text):
        suspended = []
        for index, token, value in super(JavaLexer, self).get_tokens_unprocessed(text):
            if len(suspended) > 0:
                suspended.append((index, token, value))
                if token in Text:
                    continue
                suspended.append
                if value == "(":
                    i, t, v = suspended[0]
                    suspended[0] = (i, Name.Function.Library, v)
                for item in suspended:
                    yield item
                suspended = []
            elif token in Name:
                if value in self.PROCESSING_BUILTINS:
                    if token in Name.Function:
                        yield index, Name.Function.Builtin, value
                    else:
                        yield index, Name.Variable.Builtin, value
                elif value in self.PROCESSING_LIBRARY:
                    if token in Name.Function:
                        yield index, Name.Function.Library, value
                    elif token in Name:
                        suspended.append((index, token, value))
                        continue
                    yield index, token, value
                elif value in self.PROCESSING_CONSTANTS:
                    yield index, Name.Variable.Constant, value
                elif value in self.PROCESSING_TYPES:
                    yield index, Keyword.Type, value
                else:
                    yield index, token, value
            elif value == 'void':
                yield index, Keyword.Type.Void, value
            else:
                yield index, token, value

class ProcessingStyle(Style):
    """
    A style made to resemble the processing IDE's style.
    """
    
    default_style = ''

    styles = {
        Name.Variable.Builtin: '#d94a7a',
        Name.Variable.Constant: '#718a62',
        Name.Function.Builtin: 'bold #006699',
        Name.Function.Library: '#006699',
        Comment: '#666666',
        String: '#7d4793',
        Keyword.Type: '#e2661a',
        Keyword.Type.Void: '#33997e',
        Keyword.Declaration: '#33997e',
    }
