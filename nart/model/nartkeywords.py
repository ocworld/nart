# -*- coding: utf-8 -*-

from datetime import datetime
from nart.model.nartkeyword import NartKeyword


class NartKeywords:
    """
    Naver realtime keyword의 반환값을 저장하는 클래스
    """
    def __init__(self, dt: datetime, items: [NartKeyword]):
        """
        :param dt: datetime.
        :param items: [NartKeyword].
        """
        self.dt = dt
        self.items = items
