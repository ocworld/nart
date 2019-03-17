# -*- coding: utf-8 -*-

import os
import csv
import tempfile
from nart.writer.writer import Writer
from nart.model.nartdata import NartData


class CSVWriter(Writer):
    """
    CSV로 실시간 검색어를 저장해준다.
    """

    def __init__(self, path=None, append_if_exist=True, encoding='utf-8', delimiter=','):
        """
        :param path: str. csv파일을 저장할 파일 경로이다.
        :param append_if_exist: bool. True: outpath에 파일이 있다면 파일의 내용을 추가한다.
                                      False: outpath에 파일이 있다면 FileExistsError 예외를 발생시킨다.
        """
        self.path = path if path else tempfile.mkstemp()
        if os.path.exists(path) and not append_if_exist:
            raise FileExistsError(f'OutCsvRepository: {self.path}')
        self.encoding = encoding
        self.delimiter = delimiter

    @classmethod
    def _to_list_for_csv(cls, data: NartData):
        """
        NartKeyword 리스트를 csv row 리스트로 변경해준다.
        :param data: NartData. 추출한 실시간검색어 리스트이다.
        :return: [str].
        """
        return [data.dt.isoformat()] + list(map(lambda item: item.keyword, data.items))

    def write(self, data: NartData):
        """
        실시간 검색어 목록을 csv에 write한다.
        :param data: 실시간 검색어 목록을 저장하고 있는 객체이다.
        """
        data_list = self._to_list_for_csv(data)

        # a: open for writing, appending to the end of the file if it exists
        with open(self.path, 'a', encoding=self.encoding) as csvfile:
            writer = csv.writer(csvfile, delimiter=self.delimiter)
            writer.writerow(data_list)
