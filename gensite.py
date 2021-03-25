#!/usr/bin/env python3
# gensite.py: Static site generator based on makesite.py.
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
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#     Copyright (c) 2018 Sunaina Pai
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be
#     included in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#     EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""Static site generator based on makesite.py."""


import os
import shutil
import re
import glob
import sys
import datetime
import hashlib
import markdown


def fread(filename):
    """Read file and close the file."""
    with open(filename, 'r') as f:
        return f.read()


def fwrite(filename, text):
    """Write content to file and close the file."""
    filename = filename + 'index.html' if filename.endswith('/') or filename == '' else filename
    filename = os.path.join('_site', filename)
    if os.path.exists(filename):
        log('W', 'Warning: Overwritting file: {}', filename)

    basedir = os.path.dirname(filename)
    if not os.path.isdir(basedir):
        os.makedirs(basedir)

    with open(filename, 'w') as f:
        f.write(text)


def log(type, msg, *args):
    """Log message with specified arguments."""
    if type == 'E' or type == 'W':  # or type == 'I':
        sys.stderr.write(msg.format(*args) + '\n')


def truncate(text, words=50):
    """Remove tags and truncate text to the specified number of words."""
    return ' '.join(re.sub('(?s)<.*?>', '', text).split()[:words]) + '...'


def urlize(name):
    """Convert string tu URL."""
    return name.lower().replace(' ', '-')


def add_to_sitemap(path, lastmod=None, freq=None, priority=None):
    """Add URL to sitemap."""
    global sitemap
    path = '<loc>https://oscarbenedito.com/' + path + '</loc>'
    if lastmod == '1970-01-01T00:00:00Z':
        lastmod = None
    lastmod = '<lastmod>' + lastmod + '</lastmod>' if lastmod else ''
    freq = '<changefreq>' + freq + '</changefreq>' if freq else ''
    priority = '<priority>' + priority + '</priority>' if priority else ''
    sitemap += '<url>' + path + lastmod + freq + priority + '</url>'


def set_redirect(src, dst):
    """Create HTML redirect."""
    fwrite(src, '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/' + dst + '"/><link rel="canonical" href="/' + dst + '"/><meta name="robots" content="noindex"></head><body><p>This page has been moved to <a href="/' + dst + '">https://oscarbenedito.com/' + dst + '</a>.</p></body></html>')
    log('I', 'Info: redirect /{} => /{}', src, dst)


def read_headers(text):
    """Parse headers in text and yield (key, value, end-index) tuples."""
    for match in re.finditer(r'\s*<!--\s*(.+?)\s*:\s*(.+?)\s*-->\s*|.+', text):
        if not match.group(1):
            break
        yield match.group(1), match.group(2), match.end()


def prettify_date(date_str):
    """Convert ISO 8601 date string to human friendly date string."""
    d = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    return d.strftime('%B %-d, %Y')


def render(template, pre=False, **params):
    """Replace placeholders in template with values from params."""
    if not pre:
        template = re.sub(r'{{\s*_if\s+([^}\s]+)\s*}}(.*?){{\s*_fi\s*}}',
                          lambda m: m.group(2) if m.group(1) in params else '',
                          template, flags=re.DOTALL)
    return re.sub(r'{{\s*([^}\s]+)\s*}}',
                  lambda m: str(params.get(m.group(1), m.group(0))),
                  template)


def read_content(filename):
    """Read content and metadata from file into a dictionary."""
    # read file content
    text = fread(filename)

    # read metadata and save it in a dictionary
    date_slug = os.path.basename(filename).split('.')[0]
    match = re.search(r'^(?:(\d\d\d\d-\d\d-\d\d)-)?(.+)$', date_slug)
    content = {
        'date': (match.group(1) or '1970-01-01') + 'T00:00:00Z',
        'slug': match.group(2)
    }

    # read headers
    end = 0
    for key, val, end in read_headers(text):
        content[key] = val

    if 'lastmod' in content:
        content['modified'] = '1'
    else:
        content['lastmod'] = content['date']

    # separate content from headers
    text = text[end:]

    # convert Markdown content to HTML
    if filename.endswith('.md'):
        text = markdown.markdown(text, extensions=['footnotes', 'fenced_code'])

    content.update({
        'content': text,
        'year': content['date'][:4],
        'month': content['date'][5:7],
        'day': content['date'][8:10],
        'date_nice': prettify_date(content['date']),
        'lastmod_nice': prettify_date(content['lastmod'])
    })

    if 'categories' in content:
        # convert the categories string to array of categories
        categories = [c.strip() for c in content['categories'].split(',')]
        categories_html = ', '.join(['<a class="p-category" href="/blog/categories/' + urlize(c) + '/">' + c + '</a>' for c in categories])
        content.update({
            'categories': categories,
            'categories_html': categories_html
        })

    return content


def make_pages(src, dst, layout, blog=False, **params):
    """Generate pages from page content."""
    items = []
    categories = {}

    for src_path in glob.glob(src):
        content = read_content(src_path)

        page_params = dict(params, **content)

        # populate placeholders in content if content-rendering is enabled
        if page_params.get('render') == 'yes':
            rendered_content = render(page_params['content'], **page_params)
            page_params['content'] = rendered_content

        page_dst = render(dst, **page_params)

        if 'url' in page_params:
            page_dst = page_params['url']
        else:
            page_params.update({'url': page_dst})

        if blog:
            page_params.update({ 'src_path': src_path, })
            items.append(page_params)
        else:
            fwrite(page_dst, render(layout, **page_params))
            pri = page_params['priority'] if 'priority' in page_params else None
            add_to_sitemap(page_dst, lastmod=page_params['lastmod'], priority=pri)
            log('I', 'Info: page {} => /{}', src_path, page_dst)

    items.sort(key=lambda x: x['date'], reverse=True)
    for i, item in enumerate(items):
        if i != 0:
            item['next_url'] = items[i-1]['url']
            item['next_title'] = items[i-1]['title']
            item['more_pages'] = '1'
        if i < len(items)-1:
            item['prev_url'] = items[i+1]['url']
            item['prev_title'] = items[i+1]['title']
            item['more_pages'] = '1'

        for category in item['categories']:
            if category not in categories:
                categories[category] = [item]
            else:
                categories[category].append(item)

        fwrite(item['url'], render(layout, **item))
        pri = item['priority'] if 'priority' in item else None
        add_to_sitemap(item['url'], lastmod=item['lastmod'], priority=pri)
        log('I', 'Info: post {} => /{}', item['src_path'], item['url'])

    return items, categories


def make_lists(posts, dst, list_layout, item_layout, src=None, **params):
    """Generate HTML lists for a blog."""
    item_per_page = 5
    items = []
    count = 1
    page_dst = dst
    text = fread(src) if src else fread('content/' + dst + '_index.md')
    end = 0
    for key, val, end in read_headers(text):
        params[key] = val
    params['intro'] = markdown.markdown(text[end:], extensions=['footnotes', 'fenced_code'])
    for i, post in enumerate(posts):
        item_params = dict(params, **post)
        item_params['summary'] = truncate(post['content'])
        items.append(render(item_layout, **item_params))
        if i % item_per_page == item_per_page-1 and len(posts)-1 > i:
            params['more_pages'] = '1'
            params['content'] = ''.join(items)
            params['next_url'] = dst + 'page/' + str(count+1) + '/'
            if count != 1:
                params['prev_url'] = dst + ('page/' + str(count-1) + '/' if count != 2 else '')
            fwrite(page_dst, render(list_layout, **params))
            log('I', 'Info: list => /{}', page_dst)
            count = count+1
            page_dst = dst + 'page/' + str(count) + '/'
            items = []

    if count != 1:
        del params['next_url']
        params['prev_url'] = dst + ('page/' + str(count-1) + '/' if count != 2 else '')
    params['content'] = ''.join(items)
    fwrite(page_dst, render(list_layout, **params))
    log('I', 'Info: list => /{}', page_dst)

    set_redirect(dst + 'page/1/', dst)


def make_feed(posts, dst, list_layout, item_layout, **params):
    """Generate feed for a blog."""
    max = 15
    params['url'] = dst
    page_dst = dst + 'index.xml'
    items = []
    for i, post in enumerate(posts):
        if (i == max):
            break
        item_params = dict(params, **post)
        item_params['c_escaped'] = post['content'].replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
        item = render(item_layout, **item_params)
        items.append(item)

    params['content'] = ''.join(items)
    params['updated'] = posts[0]['lastmod']
    fwrite(page_dst, render(list_layout, **params))
    log('I', 'Info: feed => /{}', page_dst)


def make_archive(posts, categories, dst, layout, **params):
    year = 0
    params['content'] = '<h2>Posts (' + str(len(posts)) + ')</h2>\n'
    for post in posts:
        if post['year'] != year:
            params['content'] += ('</ul>\n' if year != 0 else '') + '<h3>' + post['year'] + '</h3>\n<ul>\n'
            year = post['year']
        params['content'] += '<li><a href="/' + post['url'] + '">' + post['title'] + '</a> (' + post['date_nice'][:-6] + ')</li>\n'
    params['content'] += '</ul>\n'

    params['content'] += '<h2>Categories (' + str(len(categories)) + ')</h2>\n<ul>\n'
    for key in sorted(categories):
        val = categories[key]
        params['content'] += '<li><a href="/' + dst + 'categories/' + urlize(key) + '/">' + key + '</a> (' + str(len(val)) + (' entry' if len(val) == 1 else ' entries') + ')</li>\n'
    params['content'] += '</ul>\n'

    page_dst = dst + 'archive/'
    fwrite(page_dst, render(layout, **params))
    add_to_sitemap(page_dst, lastmod=posts[0]['lastmod'], priority='0.4')
    log('I', 'Info: page => /{}', page_dst)


def main():
    # create a new _site directory from scratch
    if os.path.isdir('_site'):
        shutil.rmtree('_site')
    shutil.copytree('static', '_site')

    # initialize parameters
    params = {}

    # initialize sitemap
    global sitemap
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    # copy assets adding part of their sha256 value to the filename
    for path, _, files in os.walk('assets'):
        for name in files:
            file = os.path.join(path, name)
            rfile = os.path.relpath(file, 'assets')
            with open(file, 'r') as c:
                content = c.read()

            # minify css
            if os.path.splitext(file)[1] == '.css':
                content = re.sub('\s*/\*(?:.|\n)*?\*/\s*', '', content)
                content = re.sub('\s+', ' ', content)
                content = re.sub('\s*({|}|;|,)\s*', r'\1', content)
                content = re.sub(':\s*', ':', content)
                rfile = '{0}.min{1}'.format(*os.path.splitext(rfile))

            h = hashlib.sha256()
            h.update(content.encode('utf-8'))
            name, ext = os.path.splitext(rfile)
            dst = '{n}.{h}{e}'.format(n=name, h=h.hexdigest()[:8], e=ext)

            params['_asset_' + rfile] = dst
            basedir = os.path.dirname(os.path.join('_site', dst))
            if not os.path.isdir(basedir):
                os.makedirs(basedir)
            with open(os.path.join('_site', dst), 'w') as c:
                c.write(content)

    # load layouts
    base_layout = fread('layouts/base.html')
    page_layout = fread('layouts/page.html')
    post_layout = fread('layouts/post.html')
    list_html = fread('layouts/list.html')
    item_html = fread('layouts/item.html')
    feed_xml = fread('layouts/feed.xml')
    item_xml = fread('layouts/item.xml')
    layout_404 = fread('layouts/404.html')

    # combine layouts to form final layouts
    page_layout = render(base_layout, pre=True, content=page_layout)
    post_layout = render(base_layout, pre=True, content=post_layout)
    list_html = render(base_layout, pre=True, content=list_html)

    # create site pages
    make_pages('content/_index.md', '', page_layout, **params)
    make_pages('content/[!_]*.*', '{{ slug }}/', page_layout, **params)
    fwrite('404.html', render(layout_404, **params))

    # create blog post pages
    blog_posts, categories = make_pages('content/blog/[!_]*.*',
                                        'blog/{{ year }}/{{ month }}/{{ slug }}/',
                                        post_layout, True, **params)
    # create HTML list pages
    make_lists(blog_posts, 'blog/', list_html, item_html, **params)
    add_to_sitemap('blog/', lastmod=blog_posts[0]['lastmod'], priority='1.0')
    # create Atom feeds
    make_feed(blog_posts, 'blog/', feed_xml, item_xml, title='Personal blog',
              long_title='Oscar\'s Blog', **params)
    # create blog archive
    make_archive(blog_posts, categories, 'blog/', page_layout,
                 title='Blog archive', **params)
    # create blog categories
    for name, posts in categories.items():
        dst = 'blog/categories/' + urlize(name) + '/'
        src = 'content/blog/categories/' + urlize(name) + '.md'
        lt = name + ' on Oscar\'s Blog'
        eh = '<link rel="alternate" type="application/atom+xml" title="' + lt + '" href="/' + dst + 'index.xml"/>'
        make_lists(posts, dst, list_html, item_html, src=src, title=name,
                   extraheader=eh, **params)
        make_feed(posts, dst, feed_xml, item_xml, title=name, long_title=lt,
                  **params)

    # set redirections
    set_redirect('licenses/agpl-v3/', 'licenses/agpl-3.0.txt')
    set_redirect('licenses/gpl-v3/', 'licenses/gpl-3.0.txt')
    set_redirect('licenses/cc-by-4.0/', 'licenses/cc-by-4.0.txt')
    set_redirect('composer/', 'projects/composer/composer.html')

    fwrite('sitemap.xml', sitemap + '</urlset>')


if __name__ == '__main__':
    main()
