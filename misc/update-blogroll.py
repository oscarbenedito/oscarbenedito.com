#!/usr/bin/env python3
# Update Blogroll: updates blogroll page and OMPL file.
# Copyright (C) 2020 Oscar Benedito <oscar@oscarbenedito.com>
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

import xml.etree.ElementTree
import re


tree = xml.etree.ElementTree.parse('misc/blogroll.ompl')
root = tree.getroot()

blogs = []
for category in root[0]:
    if category.attrib['text'] == 'Blogroll':
        for entry in category:
            blogs.append({
                'text': entry.attrib['text'],
                'html': entry.attrib['htmlUrl'],
                'feed': entry.attrib['xmlUrl']
            })
        break

ompl = '<?xml version="1.0" encoding="utf-8"?>\n<opml version="1.0">\n  <head>\n    <title>Oscar Benedito\'s Blogroll</title>\n  </head>\n  <body>\n    <outline text="Oscar Benedito\'s Blogroll">\n'
md = '<!-- blogroll -->\n'

for blog in sorted(blogs, key=lambda i: i['text'].lower()):
    ompl += '      <outline type="rss" text="' + blog['text'] + '" xmlUrl="' + blog['feed'] + '" htmlUrl="' + blog['html'] + '"/>\n'
    md += '- [' + blog['text'] + '](' + blog['html'] + ') — [Feed](' + blog['feed'] + ')\n'

ompl += '    </outline>\n  </body>\n</opml>\n'
md += '<!-- /blogroll -->'

with open('static/blogroll/blogroll.ompl', 'w') as f:
    f.write(ompl)

with open('content/blogroll.md', 'r') as f:
    text = f.read()

re.sub('<!-- blogroll -->.*<!-- /blogroll -->', md, text, flags=re.DOTALL)

with open('content/blogroll.md', 'w') as f:
    f.write(text)