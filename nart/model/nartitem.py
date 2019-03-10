# -*- coding: utf-8 -*-


class NartItem:
    """
    Naver realtime keyword의 반환값을 저장하는 클래스
    """
    def __init__(self, rank: int, keyword: str):
        """
        :param rank: int. 실시간 검색어 순위
        :param keyword: str. 실시간 검색어 키워드
        """
        self.rank = rank
        self.keyword = keyword
