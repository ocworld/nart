# -*- coding: utf-8 -*-

import abc
from nart.model.nartdata import NartData


class DataSource(metaclass=abc.ABCMeta):
    """
    실시간 검색어 키워드를 반환하는 datasource를 정의한다.
    """
    @property
    @abc.abstractmethod
    def realtimekeywords(self) -> NartData:
        """
        실시간 검색어 키워드 목록을 반환한다.
        :return: NartData. 실시간 검색어 키워드 목록이다.
        """
        pass
