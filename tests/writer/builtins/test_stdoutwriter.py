# -*- coding: utf-8 -*-

import pytest
import os
import sys
import tempfile
from datetime import datetime
from nart.writer.builtins.stdoutwriter import StdOutWriter
from nart.model.nartdata import NartData
from nart.model.nartitem import NartItem


@pytest.fixture
def stdoutwriter_fixture():
    fd, filepath = tempfile.mkstemp()
    os.close(fd)

    yield filepath

    if os.path.exists(filepath):
        os.remove(filepath)


def test_stdoutwriter_success(stdoutwriter_fixture):
    """
    OutStdoutRepositoryd의 성공 테스트이다.

    :param outstdoutrepo_fixture: fixture이다.
    """
    filepath = stdoutwriter_fixture

    rank1 = NartItem(1, 'test1')
    rank2 = NartItem(2, 'test2')
    keywords = NartData(datetime.now(), [rank1, rank2])

    with open(filepath, mode='w', encoding='utf-8') as outfile:
        sys.stdout = outfile
        writer = StdOutWriter()
        writer.write(keywords)

    with open(filepath, mode='r', encoding='utf-8') as outfile:
        lines = outfile.readlines()
        assert lines[1].rstrip() == StdOutWriter.PRINT_KEYWORD_FORMAT.format(1, 'test1')
        assert lines[2].rstrip() == StdOutWriter.PRINT_KEYWORD_FORMAT.format(2, 'test2')
