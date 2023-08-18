#!/usr/bin/env python3
# gensite.py: Static site generator based on makesite.py.
# Copyright (C) 2020-2021 Oscar Benedito <oscar@oscarbenedito.com>
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


def fread(filename):
    """Read file and close the file."""
    with open(filename, 'r') as f:
        return f.read()


def fwrite(filename, text):
    """Write content to file and close the file."""
    filename = filename + 'index.html' if filename.endswith('/') or filename == '' else filename
    filename = os.path.join('_site', filename)
    if os.path.exists(filename):
        log('W', 'Overwritting file: {}', filename)

    basedir = os.path.dirname(filename)
    if not os.path.isdir(basedir):
        os.makedirs(basedir)

    with open(filename, 'w') as f:
        f.write(text)


def log(type, msg, *args):
    """Log message with specified arguments."""
    if type == 'E':
        sys.stderr.write('Error: ' + msg.format(*args) + '\n')
        sys.exit(1)
    if type == 'W':
        sys.stderr.write('Warning: ' + msg.format(*args) + '\n')
    # if type == 'I':
    #     sys.stderr.write('Info: ' + msg.format(*args) + '\n')


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
    fwrite(src, '<!DOCTYPE html><html><head><meta charset="utf-8">'
                '<meta http-equiv="refresh" content="0; url=/{}"/>'
                '<link rel="canonical" href="/{}"/><meta name="robots" content="noindex">'
                '</head><body><p>This page has been moved to '
                '<a href="/{}">https://oscarbenedito.com/{}</a>.</p>'
                '</body></html>'.format(dst, dst, dst, dst))
    log('I', 'redirect /{} => /{}', src, dst)
    # uncomment next line to print apache redirects
    # sys.stdout.write('Redirect permanent "/{}" "/{}"\n'.format(src, dst))


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
        template = re.sub(r'{{\s*_ife\s+([^}\s]+)\s*}}(.*?){{\s*_else\s*}}(.*?){{\s*_fi\s*}}',
                          lambda m: m.group(2) if m.group(1) in params else m.group(3),
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
    # if filename.endswith('.md'):
    #     import markdown
    #     text = markdown.markdown(text, extensions=['footnotes', 'fenced_code'])

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

        if 'url' not in page_params:
            page_params['url'] = render(dst, **page_params)
        else:   # can be deleted, just to warn since I have never used it
            log('W', 'parameter \'url\' set in {}', src_path)

        if blog:
            page_params['src_path'] = src_path
            items.append(page_params)
        else:
            fwrite(page_params['url'], render(layout, **page_params))
            pri = page_params['priority'] if 'priority' in page_params else None
            add_to_sitemap(page_params['url'], lastmod=page_params['lastmod'], priority=pri)
            log('I', 'page {} => /{}', src_path, page_params['url'])

    # the following is only executed if blog == True, otherwise items is empty
    items.sort(key=lambda x: x['date'], reverse=True)
    for i, item in enumerate(items):
        if i != 0:
            item['next_url'] = items[i-1]['url']
            item['next_title'] = items[i-1]['title']
            item['multiple_pages'] = '1'
        if i < len(items)-1:
            item['prev_url'] = items[i+1]['url']
            item['prev_title'] = items[i+1]['title']
            item['multiple_pages'] = '1'

        for category in item['categories']:
            if category not in categories:
                categories[category] = [item]
            else:
                categories[category].append(item)

        fwrite(item['url'], render(layout, **item))
        pri = item['priority'] if 'priority' in item else None
        add_to_sitemap(item['url'], lastmod=item['lastmod'], priority=pri)
        log('I', 'post {} => /{}', item['src_path'], item['url'])

    return items, categories


def make_lists(posts, dst, l_html, l_html_item, l_feed, l_feed_item, **params):
    """Generate HTML lists and Atom feed for a set of posts."""
    if os.path.isfile('content/' + dst + '_index.html'):
        text = fread('content/' + dst + '_index.html')
    else:
        text = fread('content/' + dst[:-1] + '.html')
    end = 0

    for key, val, end in read_headers(text):
        params[key] = val

    params['intro'] = text[end:]

    # make HTML lists
    ipp = 5     # items per page
    params['content'] = ''
    title = params['title']
    if dst != 'blog/':  # blog feed appears on all pages already
        params['extraheader'] = '<link rel="alternate" type="application/atom+xml" ' \
                                'title="{}" href="/{}index.xml"/>'.format(params['feed_title'], dst)

    for i, post in enumerate(posts):
        item_params = dict(params, **post)

        # remove tags and truncate at 50 words
        item_params['summary'] = ' '.join(re.sub('(?s)<.*?>', '', post['content']).split()[:50]) + '...'

        params['content'] += render(l_html_item, **item_params)

        if i % ipp == ipp-1 or i == len(posts)-1:
            page = i//ipp + 1
            curr_dst = dst + ('page/{}/'.format(page) if i >= ipp else '')

            if i != len(posts)-1:
                params['multiple_pages'] = '1'
                params['next_url'] = '{}page/{}/'.format(dst, page + 1)
            elif page > 1:
                params.pop('next_url')

            if page != 1:
                params['title'] = '{} (page {} of {})'.format(title, page, ((len(posts)-1)//ipp) + 1)

            fwrite(curr_dst, render(l_html, **params))
            log('I', 'list => /{}', curr_dst)

            params['prev_url'] = curr_dst
            params['content'] = ''

    set_redirect(dst + 'page/1/', dst)

    # make Atom feed
    ipp = 15    # item per feed
    params['url'] = dst
    page_dst = dst + 'index.xml'
    params['content'] = ''
    for i, post in enumerate(posts):
        if (i == ipp):
            break
        item_params = dict(params, **post)

        # escape HTML content
        item_params['c_escaped'] = post['content'].replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')

        params['content'] += render(l_feed_item, **item_params)

    params['updated'] = posts[0]['lastmod']
    fwrite(page_dst, render(l_feed, **params))
    log('I', 'feed => /{}', page_dst)


def make_archive(posts, categories, dst, layout, **params):
    year = 0
    params['content'] = '<h2>Posts ({})</h2>\n'.format(len(posts))
    for post in posts:
        if post['year'] != year:
            params['content'] += '</ul>\n' if year != 0 else ''
            params['content'] += '<h3>{}</h3>\n<ul>\n'.format(post['year'])
            year = post['year']
        params['content'] += '<li><a href="/{}">{}</a> ({})</li>\n' \
                             ''.format(post['url'], post['title'], post['date_nice'][:-6])
    params['content'] += '</ul>\n'

    params['content'] += '<h2>Categories ({})</h2>\n<ul>\n'.format(len(categories))
    for key in sorted(categories):
        val = categories[key]
        params['content'] += '<li><a href="/{}categories/{}/">{}</a> ({} {})</li>\n' \
                             ''.format(dst, urlize(key), key, len(val), 'entry' if len(val) == 1 else 'entries')
    params['content'] += '</ul>\n'

    page_dst = dst + 'archive/'
    fwrite(page_dst, render(layout, **params))
    add_to_sitemap(page_dst, lastmod=posts[0]['lastmod'], priority='0.4')
    log('I', 'page => /{}', page_dst)


def main():
    # create a new _site directory from scratch
    if os.path.isdir('_site'):
        shutil.rmtree('_site')
    shutil.copytree('static', '_site')

    # initialize parameters
    params = {}

    # initialize sitemap
    global sitemap
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n' \
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    # copy assets adding part of their sha256 value to the filename
    for path, _, files in os.walk('assets'):
        for name in files:
            file = os.path.join(path, name)
            rfile = os.path.relpath(file, 'assets')
            with open(file, 'r') as c:
                content = c.read()

            # minify css
            if os.path.splitext(file)[1] == '.css':
                content = re.sub(r'\s*/\*(?:.|\n)*?\*/\s*', '', content)
                content = re.sub(r'\s+', ' ', content)
                content = re.sub(r'\s*({|}|;|,)\s*', r'\1', content)
                content = re.sub(r':\s*', ':', content)
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
    l_base = fread('layouts/base.html')
    l_page = render(l_base, pre=True, content=fread('layouts/page.html'))
    l_post = render(l_base, pre=True, content=fread('layouts/post.html'))
    l_list = render(l_base, pre=True, content=fread('layouts/list.html'))
    l_feed = fread('layouts/feed.xml')
    item_html = fread('layouts/item.html')
    item_xml = fread('layouts/item.xml')

    # create site pages
    make_pages('content/_index.html', '', l_page, **params)
    make_pages('content/[!_]*.*', '{{ slug }}/', l_page, **params)
    make_pages('content/projects/[!_]*.*', 'projects/{{ slug }}/', l_page, **params)
    make_pages('content/en/_index.html', 'en/', l_page, **params)
    make_pages('content/en/[!_]*.*', 'en/{{ slug }}/', l_page, **params)
    fwrite('404.html', render(fread('layouts/404.html'), **params))

    # create blog post pages
    all_posts, categories = make_pages('content/blog/[!_]*.*',
                                       'blog/{{ year }}/{{ month }}/{{ slug }}/',
                                       l_post, blog=True, **params)

    # create HTML list pages and Atom feed
    make_lists(all_posts, 'blog/', l_list, item_html, l_feed, item_xml, **params)

    add_to_sitemap('blog/', lastmod=all_posts[0]['lastmod'], priority='1.0')

    # create blog archive
    make_archive(all_posts, categories, 'blog/', l_page, title='Blog archive', **params)

    # create blog categories
    for name, c_posts in categories.items():
        dst = 'blog/categories/' + urlize(name) + '/'
        make_lists(c_posts, dst, l_list, item_html, l_feed, item_xml, **params)

    # set redirections
    set_redirect('licenses/agpl-v3/', 'licenses/agpl-3.0.txt')
    set_redirect('licenses/gpl-v3/', 'licenses/gpl-3.0.txt')
    set_redirect('licenses/cc-by-4.0/', 'licenses/cc-by-4.0.txt')
    set_redirect('composer/', 'projects/composer/composer.html')
    set_redirect('contact/', 'en/#contact-me')
    set_redirect('about/', 'en/about/')

    fwrite('sitemap.xml', sitemap + '</urlset>')


if __name__ == '__main__':
    main()
