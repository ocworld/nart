# -*- coding: utf-8 -*-

import yaml
import os
from pathlib import Path
from nart.model.configkey import ConfigKey


class Config:
    def __init__(self, timeunit, interval, start_on_time, use_stdoutwriter, use_csvwriter, csvwriter_outpath):
        self.timeunit = timeunit
        self.interval = interval
        self.start_on_time = start_on_time
        self.use_stdoutwriter = use_stdoutwriter
        self.use_csvwriter = use_csvwriter
        self.csvwriter_outpath = csvwriter_outpath

    @classmethod
    def from_dict(cls, conf_dict):
        keys = conf_dict.keys()
        timeunit: str = conf_dict[ConfigKey.TIMEUNIT] if ConfigKey.TIMEUNIT in keys else None
        interval: int = conf_dict[ConfigKey.INTERVAL] if ConfigKey.INTERVAL in keys else None
        start_on_time: bool = conf_dict[ConfigKey.START_ON_TIME] if ConfigKey.START_ON_TIME in keys else None
        use_stdoutwriter: bool = conf_dict[ConfigKey.USE_STDOUTWRITER] if ConfigKey.USE_STDOUTWRITER in keys else None
        use_csvwriter: bool = conf_dict[ConfigKey.USE_CSVWRITER] if ConfigKey.USE_CSVWRITER in keys else None
        csvwriter_dict = conf_dict[ConfigKey.CSVWRITER] if ConfigKey.CSVWRITER in keys else None
        if csvwriter_dict:
            csvwriter_outpath = csvwriter_dict[ConfigKey.CSVWRITER_PATH] \
                if ConfigKey.CSVWRITER_PATH in csvwriter_dict.keys() else None
        else:
            csvwriter_outpath = None

        return cls(timeunit, interval, start_on_time, use_stdoutwriter, use_csvwriter, csvwriter_outpath)

    @classmethod
    def from_file(cls, path=None, encoding='utf-8'):
        if path is None:
            path = os.path.join(str(Path.home()), '.nart.yaml')

        with open(path, mode='r', encoding=encoding) as conf_file:
            conf_dict = yaml.safe_load(conf_file)

        return cls.from_dict(conf_dict)
