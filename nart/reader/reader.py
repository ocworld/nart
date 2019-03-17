# -*- coding: utf-8 -*-

import abc
from nart.model.nartdata import NartData


class Reader(metaclass=abc.ABCMeta):
    """
    네이버 실시간 검색어를 읽어주는 클래스이다.
    read에서 어떤 동작을 할지 상세 구현은 상속받은 클래스가 처리해야한다.
    """

    @abc.abstractmethod
    def read(self) -> [NartData]:
        """
        네이버 실시간 검색어 키워드를 읽어주는 함수이다.
        """
        pass

    @abc.abstractmethod
    def iter_read(self):
        """
        네이버 실시간 검색어 키워드를 읽어주는 함수이다.
        """
        pass
