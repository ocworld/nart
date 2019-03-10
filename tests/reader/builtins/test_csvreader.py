# -*- coding: utf-8 -*-

import pytest
import os
from pathlib import Path
from nart.reader.builtins.csvreader import CSVReader


@pytest.fixture()
def get_reader_test_csv_path():
    cur_path = os.path.realpath(__file__)
    builtins_path = Path(cur_path).parent
    reader_path = Path(builtins_path).parent
    tests_path = Path(reader_path).parent
    resources_path = os.path.join(tests_path, 'resources')
    test_csv_path = os.path.join(resources_path, 'reader_test.csv')
    yield test_csv_path


def test_csvreader_read_success(get_reader_test_csv_path):
    test_csv_path = get_reader_test_csv_path
    assert os.path.exists(test_csv_path)

    reader = CSVReader(test_csv_path)
    data_list = reader.read()

    assert len(data_list) == 2
    assert len(data_list[0].items) == 20
    assert len(data_list[1].items) == 20


def test_csvreader_iter_read_success(get_reader_test_csv_path):
    test_csv_path = get_reader_test_csv_path
    assert os.path.exists(test_csv_path)

    reader = CSVReader(test_csv_path)

    data_list = []
    for data in reader.iter_read():
        assert len(data.items) == 20
        data_list.append(data)

    assert len(data_list) == 2



