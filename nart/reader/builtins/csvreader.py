# -*- coding: utf-8 -*-

import csv
from datetime import datetime
from nart.reader.reader import Reader
from nart.model.nartdata import NartData
from nart.model.nartitem import NartItem


class CSVReader(Reader):

    def __init__(self, path, encoding='utf-8', delimiter=','):
        self.path = path
        self.encoding = encoding
        self.delimiter = delimiter

    @classmethod
    def get_data_from_csvrow(cls, row: str) -> NartData:
        dt_iso_str = row[0]
        dt = datetime.fromisoformat(dt_iso_str)

        rank = 1
        items: [NartItem] = []
        for keyword in row[1:]:
            items.append(NartItem(rank=rank, keyword=keyword))
            rank = rank + 1

        return NartData(dt, items)

    def read(self) -> [NartData]:

        data_list: [NartData] = []

        with open(file=self.path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            for row in reader:
                data_list.append(self.get_data_from_csvrow(row))

        return data_list

    def iter_read(self):
        with open(file=self.path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            for row in reader:
                yield self.get_data_from_csvrow(row)
