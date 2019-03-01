# -*- coding: utf-8 -*-

import pytest
import os
import sys
import tempfile
from datetime import datetime
from nart.out.builtins.outstdoutrepository import OutStdoutRepository
from nart.model.nartkeywords import NartKeywords
from nart.model.nartkeyword import NartKeyword


@pytest.fixture
def outstdoutrepo_fixture():
    fd, filepath = tempfile.mkstemp()
    os.close(fd)

    yield filepath

    if os.path.exists(filepath):
        os.remove(filepath)


def test_outstdoutrepository_success(outstdoutrepo_fixture):
    """
    OutStdoutRepositoryd의 성공 테스트이다.

    :param outstdoutrepo_fixture: fixture이다.
    """
    filepath = outstdoutrepo_fixture

    rank1 = NartKeyword(1, 'test1')
    rank2 = NartKeyword(2, 'test2')
    keywords = NartKeywords(datetime.now(), [rank1, rank2])

    with open(filepath, mode='w', encoding='utf-8') as outfile:
        sys.stdout = outfile
        outrepo = OutStdoutRepository()
        outrepo.write(keywords)

    with open(filepath, mode='r', encoding='utf-8') as outfile:
        lines = outfile.readlines()
        assert lines[1].rstrip() == OutStdoutRepository.PRINT_KEYWORD_FORMAT.format(1, 'test1')
        assert lines[2].rstrip() == OutStdoutRepository.PRINT_KEYWORD_FORMAT.format(2, 'test2')
