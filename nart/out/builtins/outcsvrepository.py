# -*- coding: utf-8 -*-

import os
import csv
import tempfile
from nart.out.outrepository import OutRepository
from nart.model.nartkeywords import NartKeywords


class OutCsvRepository(OutRepository):
    """
    CSV로 실시간 검색어를 저장해준다.
    """

    def __init__(self, outpath=None, append_if_exist=True):
        """
        :param outpath: str. csv파일을 저장할 파일 경로이다.
        :param append_if_exist: bool. True: outpath에 파일이 있다면 파일의 내용을 추가한다.
                                      False: outpath에 파일이 있다면 FileExistsError 예외를 발생시킨다.
        """
        self.outpath = outpath if outpath else tempfile.mkstemp()
        if os.path.exists(outpath) and not append_if_exist:
            raise FileExistsError(f'OutCsvRepository: {self.outpath}')

    @classmethod
    def _to_list_for_csv(cls, keywords: NartKeywords):
        """
        NartKeyword 리스트를 csv row 리스트로 변경해준다.
        :param keywords: NartKeywords. 추출한 실시간검색어 리스트이다.
        :return: [str].
        """
        return [keywords.dt.isoformat()] + list(map(lambda item: item.keyword, keywords.items))

    def write(self, keywords: NartKeywords):
        """
        실시간 검색어 목록을 csv에 write한다.
        :param keywords: 실시간 검색어 목록을 저장하고 있는 객체이다.
        """
        data_list = self._to_list_for_csv(keywords)

        # a: open for writing, appending to the end of the file if it exists
        with open(self.outpath, 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data_list)
