# -*- coding: utf-8 -*-

import schedule
import time
from nart.datasource.datasource import DataSource
from nart.datasource.builtins.htmlparsedatasource import HtmlParseDataSource
from nart.writer.writer import Writer


class Nart:
    """
    정해진 스케쥴 단위로 네이버 실시간 검색어를 가져와서 outrepos에 출력해주는 서비스이다.
    """

    def __init__(self, writers: [Writer], datasource: DataSource = None):
        """
        :param writers: [Writer]. 실시간 검색어를 출력해줄 writer목록이다.
        :param datasource: DataSource. 실시간 검색어를 가져올 datasource이다.
                                       기본값은 Html Parsing이다.
        """
        self.writers = writers
        self.datasource = datasource if datasource else HtmlParseDataSource()

    def write_nart(self):
        """
        naver 실시간 검색어 키워드를 writer로 저장한다.
        """
        keywords = self.datasource.realtimekeywords
        for writer in self.writers:
            writer.write(keywords)

    def run_with_hour(self, interval=1, start_on_the_hour=False):
        """
        시간(hour) 간격으로 실시간 검색어 키워드 목록을 가져와서 저장한다.

        :param interval: int. 시간(hour) 단위이다. 예를 들어, 1이면 1시간, 2이면 2시간 간격으로 가져온다.
        :param start_on_the_hour: bool. 정각에 시작하는지를 결정한다. True이면 00분에 가까운 시간에 시작한다.
        """
        if start_on_the_hour:
            schedule.every(interval).hours.at(':00').do(self.write_nart)
        else:
            schedule.every(interval).hours.do(self.write_nart)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def run_with_min(self, interval=1, start_on_the_min=False):
        """
        분(min) 간격으로 실시간 검색어 키워드 목록을 가져와서 저장한다.

        :param interval: int. 분(min) 단위이다. 예를 들어, 1이면 1시간, 2이면 2시간 간격으로 가져온다.
        :param start_on_the_min: bool. 정각에 시작하는지를 결정한다. True이면 00분에 가까운 시간에 시작한다.
        """
        if start_on_the_min:
            schedule.every(interval).minutes.at(':00').do(self.write_nart)
        else:
            schedule.every(interval).minutes.do(self.write_nart)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def run_with_sec(self, interval=1):
        """
        초(sec) 간격으로 실시간 검색어 키워드 목록을 가져와서 저장한다.

        :param interval: int. 분(min) 단위이다. 예를 들어, 1이면 1시간, 2이면 2시간 간격으로 가져온다.
        :param max_num: int. 최대 작업 횟수이다. 이 값이 None이면 중지 없이 계속 작업한다.
        """
        schedule.every(interval).seconds.do(self.write_nart)

        while True:
            schedule.run_pending()
            time.sleep(0.1)
