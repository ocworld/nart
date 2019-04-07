# -*- coding: utf-8 -*-

from enum import Enum


class Timeunit(Enum):
    SEC = 0
    MIN = 1
    HOUR = 2

    @classmethod
    def from_str(cls, unit_str):
        return {
            'sec': cls.SEC,
            'second': cls.SEC,
            'seconds': cls.SEC,
            'min': cls.MIN,
            'minute': cls.MIN,
            'minutes': cls.MIN,
            'hour': cls.HOUR,
            'hours': cls.HOUR,
        }[unit_str]
