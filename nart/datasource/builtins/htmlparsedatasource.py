# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from bs4 import BeautifulSoup
from nart.datasource.datasource import DataSource
from nart.model.nartitem import NartItem
from nart.model.nartdata import NartData


class HtmlParseDataSource(DataSource):
    """
    naver 홈페이지로부터 html을 파싱해서 실시간 검색어를 가져온다.
    """

    NAVER_URL = 'https://www.naver.com/'

    @property
    def realtimekeywords(self) -> NartData:
        """
        naver 실시간 검색어 키워드를 반환한다.
        naver 홈페이지로부터 html을 파싱해서 가져온다

        :return: NartKeywords. 순위와 키워드로 구성된 리스트
        """
        html = requests.get(self.NAVER_URL).text
        soup = BeautifulSoup(html, 'html.parser')
        rt_keyword_tags = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
        rt_keywords = [NartItem(rank=idx, keyword=keyword.text) for idx, keyword in enumerate(rt_keyword_tags)]
        return NartData(datetime.now(), rt_keywords)

