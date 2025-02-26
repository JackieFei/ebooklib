# This file is part of EbookLib.
# Copyright (c) 2013 Aleksandar Erkalovic <aerkalov@gmail.com>
#
# EbookLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# EbookLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with EbookLib.  If not, see <http://www.gnu.org/licenses/>.

import io
import mimetypes

from lxml import etree


mimetype_initialised = False


def debug(obj):
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(obj)


def parse_string(s):
    try:
        tree = etree.parse(io.BytesIO(s.encode('utf-8')))
    except:
        tree = etree.parse(io.BytesIO(s))

    return tree


def parse_html_string(s):
    from lxml import html

    utf8_parser = html.HTMLParser(encoding='utf-8')

    html_tree = html.document_fromstring(s, parser=utf8_parser)

    return html_tree


def guess_type(extenstion):
    global mimetype_initialised

    if not mimetype_initialised:
        mimetypes.init()
        mimetypes.add_type('application/xhtml+xml', '.xhtml')
        mimetype_initialised = True

    # print ('ebooklib/utils guess_type extenstion =', extenstion)
    # 2022/05/18 這種寫法可以在 AWS Lambda 成功執行
    #   [ERROR] AttributeError: module 'urllib3.packages.six.moves.urllib_parse' has no attribute '_splittype'
    #     File "/var/lang/lib/python3.8/mimetypes.py", line 117, in guess_type
    #       scheme, url = urllib.parse._splittype(url)
    # return mimetypes.MimeTypes().guess_type(extenstion)
    return mimetypes.guess_type(extenstion)
