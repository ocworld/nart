# -*- coding: utf-8 -*-

from nart.writer.writer import Writer
from nart.model.nartdata import NartData


class StdOutWriter(Writer):
    """
    stdout값으로 실시간 검색어 목록을 출력해준다.
    """

    PRINT_KEYWORD_FORMAT = '{}: {}'

    def write(self, data: NartData):
        """
        실시간 검색어 목록을 stdout으로 출력한다.
        :param data: 실시간 검색어 목록을 저장하고 있는 객체이다.
        """

        print(f'datetime: {data.dt.isoformat()}')
        for item in data.items:
            print(self.PRINT_KEYWORD_FORMAT.format(item.rank, item.keyword))
