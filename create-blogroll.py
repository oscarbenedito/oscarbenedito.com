#!/usr/bin/env python3
#
# Create Blogroll: creates the JSON for a blogroll's page from an OMPL file.
#
# Copyright (C) 2020 Oscar Benedito
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

import sys
import json
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

out = []
for category in root[0]:
    if category.attrib['text'] == "Blogroll":
        for entry in category:
            out.append({
                "name": entry.attrib['text'],
                "url": entry.attrib['htmlUrl'],
                "feed": entry.attrib['xmlUrl']
            })
        break

print(json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False))
