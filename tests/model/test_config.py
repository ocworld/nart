# -*- coding: utf-8 -*-

import pytest
import os
from pathlib import Path
from nart.model.config import Config


@pytest.fixture()
def get_config_path():
    cur_path = os.path.realpath(__file__)
    model_path = Path(cur_path).parent
    tests_path = Path(model_path).parent
    resources_path = os.path.join(tests_path, 'resources')
    test_csv_path = os.path.join(resources_path, 'config.yaml')
    yield test_csv_path


def test_config_success(get_config_path):
    # timeunit: min
    # interval: 1
    # start_on_time: true
    # use_stdoutwriter: true
    # use_csvwriter: true
    # csvwriter:
    # path: '/tmp/nart.csv'
    cfg = Config.from_file(get_config_path)
    assert cfg.timeunit == 'min'
    assert cfg.interval == 1
    assert cfg.start_on_time is True
    assert cfg.use_stdoutwriter is True
    assert cfg.use_csvwriter is True
    assert cfg.csvwriter_outpath == '/tmp/nart.csv'
