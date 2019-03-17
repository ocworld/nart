# -*- coding: utf-8 -*-

import csv
from datetime import datetime
from nart.reader.reader import Reader
from nart.model.nartdata import NartData
from nart.model.nartitem import NartItem


class CSVReader(Reader):
    """
    CSVWriter로 저장한 실시간 검색어 키워드를 읽어오기 위한 클래스이다.
    """

    def __init__(self, path, encoding='utf-8', delimiter=','):
        """
        :param path: 읽어올 csv 파일 경로이다.
        :param encoding: 읽어올 csv 파일의 인코딩이다.
        :param delimiter: 읽어올 csv 파일의 delimiter이다.
        """
        self.path = path
        self.encoding = encoding
        self.delimiter = delimiter

    @classmethod
    def get_data_from_csvrow(cls, row: str) -> NartData:
        """
        csv파일의 행으로부터 NartData 객체를 읽어와서 반환한다.

        :param row: csv 파일의 row이다.
        :return: NartData.
        """
        dt_iso_str = row[0]
        dt = datetime.fromisoformat(dt_iso_str)

        rank = 1
        items: [NartItem] = []
        for keyword in row[1:]:
            items.append(NartItem(rank=rank, keyword=keyword))
            rank = rank + 1

        return NartData(dt, items)

    def read(self) -> [NartData]:
        """
        csv 파일로부터 읽은 NartData 객체리스트를 반환한다.

        :return: [NartData].
        """
        with open(file=self.path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            data_list = list(map(lambda row: self.get_data_from_csvrow(row), reader))

        return data_list

    def iter_read(self):
        """
        csv 파일을 읽어 generator (yield)로 반환한다.

        :yield: yield로 반환되는 generator의 NartData이다.
        """
        with open(file=self.path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            for row in reader:
                yield self.get_data_from_csvrow(row)
