#    LPTP
#    Copyright (C) 2024-2525  ko114

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import mistune
from mistune.directives import RSTDirective, TableOfContents, Admonition
import bleach
allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'br',
                'h1', 'h2', 'h3', 'p', 'h4', 'h5', 'h6', 'sub', 'sup', 'img', 'hr'
                 'ins', 'q', 'del', 'table', 'tr', 'td',
                'mark', 'ruby', 'rp', 'rt', 'div', 'span']
md = mistune.create_markdown(escape=False, plugins=['strikethrough', 'footnotes', 'table',
                                                    'task_lists', 'def_list', 'abbr', 'mark',
                                                    'insert', 'superscript', 'subscript', 'ruby', 'math',
                                                    RSTDirective([
                                                        TableOfContents(), Admonition()
                                                    ]),
                                                    ])
ALLOWED_ATTRIBUTES = {
    "a": ["href", "title"],
    "abbr": ["title"],
    "acronym": ["title"],
    'img': ['alt', 'title', 'src'],
}

def clean_html(html):
    return (bleach.clean(html, tags=allowed_tags, strip=False, attributes=ALLOWED_ATTRIBUTES)
            .replace('&lt;hr /&gt;','<hr/>'))

def render_md(markdown):
    return md(markdown)