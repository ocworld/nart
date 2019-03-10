# -*- coding: utf-8 -*-

import pytest
import os
import csv
import tempfile
from datetime import datetime
from nart.writer.builtins.csvwriter import CSVWriter
from nart.model.nartdata import NartData
from nart.model.nartitem import NartItem


@pytest.fixture
def csvwriter_fixture():
    """
    csvrepo의 filepath를 생성하고, 테스트가 끝난 뒤 제거한다.

    :return: str. filepath. csvrepo의 filepath이다.
    """
    fd, filepath = tempfile.mkstemp()
    os.close(fd)

    yield filepath

    if os.path.exists(filepath):
        os.remove(filepath)


def test_csvwriter_success(csvwriter_fixture):
    """
    CSVWriter의 성공 테스트이다.

    :param csvwriter_fixture: fixture이다.
    """
    filepath = csvwriter_fixture

    rank1 = NartItem(1, 'test1')
    rank2 = NartItem(2, 'test2')
    keywords = NartData(datetime.now(), [rank1, rank2])

    writer = CSVWriter(path=filepath, append_if_exist=True)
    writer.write(keywords)

    assert os.path.exists(writer.path)

    with open(writer.path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader_count = 0

        for row in reader:
            reader_count = reader_count + 1
            assert row[1] == 'test1'
            assert row[2] == 'test2'

        assert reader_count == 1
