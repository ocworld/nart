# -*- coding: utf-8 -*-

import abc
from nart.model.nartdata import NartData


class Writer(metaclass=abc.ABCMeta):
    """
    네이버 실시간 검색어를 저장해주는 클래스이다.
    Nart내부에서 write만 호출한다.
    write에서 어떤 동작을 할지 상세 구현은 상속받은 클래스가 처리해야한다.
    """

    @abc.abstractmethod
    def write(self, data: NartData):
        """
        네이버 실시간 검색어 키워드를 써주는 함수이다.
        :param data: NartData. 네이버 실시간 검색어 목록이다.
        """
        pass

