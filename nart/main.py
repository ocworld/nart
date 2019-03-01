#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from nart.nart import Nart
from nart.out.outrepository import OutRepository
from nart.out.builtins.outstdoutrepository import OutStdoutRepository
from nart.out.builtins.outcsvrepository import OutCsvRepository
from nart.datasource.builtins.htmlparsedatasource import HtmlParseDataSource


def main():
    parser = argparse.ArgumentParser(description='NART needs arguments')
    parser.add_argument('timeunit', type=str, help='Input schedule time unit. (hour, min, or sec)')
    parser.add_argument('-iv', '--interval', type=int, default=1,
                        help='Inverval time between collecting realtime keywords. '
                             'Timeunit is based on timeunit')
    parser.add_argument('-csv', '--csvout', type=str, help='Set the csvfilepath, if you want to write csvfile')
    parser.add_argument('-v', '--verbose', action='store_true', help='Set the flag,'
                                                                     ' if you want for results to be printed')
    parser.add_argument('-on', '--startontime', action='store_true', help='Set the flag, collecting data start'
                                                                          ' on the hour or on the min')

    args = parser.parse_args()

    outrepos: [OutRepository] = []
    if args.verbose:
        outrepos.append(OutStdoutRepository())

    if args.csvout:
        outrepos.append(OutCsvRepository(outpath=args.csvout))

    assert len(outrepos) > 0

    on_time = True if args.startontime else False
    interval = args.interval

    datasource = HtmlParseDataSource()
    nart = Nart(outrepos, datasource)

    timeunit = args.timeunit

    if timeunit == 'hour' or timeunit == 'hours':
        nart.run_with_hour(interval=interval, start_on_the_hour=on_time)
    elif timeunit == 'min' or timeunit == 'minute' or timeunit == 'minutes':
        nart.run_with_min(interval=interval, start_on_the_min=on_time)
    elif timeunit == 'sec' or timeunit == 'second' or timeunit == 'seconds':
        nart.run_with_sec(interval=interval)


if __name__ == "__main__":
    main()
