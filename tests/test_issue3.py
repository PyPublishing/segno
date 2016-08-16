# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 -- Lars Heuer - Semagia <http://www.semagia.com/>.
# All rights reserved.
#
# License: BSD License
#
"""\
Test against issue #3.
<https://github.com/heuer/segno/issues/3>

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - http://www.semagia.com/
:license:      BSD License
"""
from __future__ import unicode_literals, absolute_import
import io
from nose.tools import ok_, eq_
import segno
try:
    from .utils import matrix_looks_valid
except (ValueError, SystemError):  # Attempted relative import in non-package
    from utils import matrix_looks_valid


def test_issue_3():
    qr = segno.make_micro('test')
    eq_('M3', qr.version)
    # This fails since PNG operates with a fixed set of two colors
    qr.save(io.BytesIO(), kind='png')


def test_issue_3_autodetect_micro():
    qr = segno.make('test')
    eq_('M3', qr.version)
    # This fails since PNG operates with a fixed set of two colors
    qr.save(io.BytesIO(), kind='png')


def test_issue_3_matrix():
    qr = segno.make_micro('test')
    ok_(*matrix_looks_valid(qr.matrix))


if __name__ == '__main__':
    import nose
    nose.core.runmodule()