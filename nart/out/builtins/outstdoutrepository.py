# -*- coding: utf-8 -*-

from nart.out.outrepository import OutRepository
from nart.model.nartkeywords import NartKeywords


class OutStdoutRepository(OutRepository):
    """
    stdout값으로 실시간 검색어 목록을 출력해준다.
    """

    PRINT_KEYWORD_FORMAT = '{}: {}'

    def write(self, keywords: NartKeywords):
        """
        실시간 검색어 목록을 stdout으로 출력한다.
        :param keywords: 실시간 검색어 목록을 저장하고 있는 객체이다.
        """

        print(f'datetime: {keywords.dt.isoformat()}')
        for item in keywords.items:
            print(self.PRINT_KEYWORD_FORMAT.format(item.rank, item.keyword))
