# -*- coding: utf-8 -*-

import pytest
import os
import csv
import tempfile
from datetime import datetime
from nart.out.builtins.outcsvrepository import OutCsvRepository
from nart.model.nartkeywords import NartKeywords
from nart.model.nartkeyword import NartKeyword


@pytest.fixture
def outcsvrepo_fixture():
    """
    csvrepo의 filepath를 생성하고, 테스트가 끝난 뒤 제거한다.

    :return: str. filepath. csvrepo의 filepath이다.
    """
    fd, filepath = tempfile.mkstemp()
    os.close(fd)

    yield filepath

    if os.path.exists(filepath):
        os.remove(filepath)


def test_outcsvrepository_success(outcsvrepo_fixture):
    """
    OutCsvRepository의 성공 테스트이다.

    :param outcsvrepo_fixture: fixture이다.
    """
    filepath = outcsvrepo_fixture

    rank1 = NartKeyword(1, 'test1')
    rank2 = NartKeyword(2, 'test2')
    keywords = NartKeywords(datetime.now(), [rank1, rank2])

    outrepo = OutCsvRepository(outpath=filepath, append_if_exist=True)
    outrepo.write(keywords)

    assert os.path.exists(outrepo.outpath)

    with open(outrepo.outpath, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader_count = 0

        for row in reader:
            reader_count = reader_count + 1
            assert row[1] == 'test1'
            assert row[2] == 'test2'

        assert reader_count == 1
