#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from nart.nart import Nart
from nart.model.config import Config
from nart.model.timeunit import Timeunit
from nart.writer.writer import Writer
from nart.writer.builtins.stdoutwriter import StdOutWriter
from nart.writer.builtins.csvwriter import CSVWriter
from nart.datasource.builtins.htmlparsedatasource import HtmlParseDataSource


def main():
    parser = argparse.ArgumentParser(description='NART needs arguments')
    parser.add_argument('-f', '--file', type=str, help='configuration file path.')
    parser.add_argument('-u', '--timeunit', type=str, help='Input schedule time unit. (hour, min, or sec)')
    parser.add_argument('-iv', '--interval', type=int, help='Inverval time between collecting realtime keywords. '
                                                            'Timeunit is based on timeunit')
    parser.add_argument('-csv', '--csvout', type=str, help='Set the csvfilepath, if you want to write csvfile')
    parser.add_argument('-v', '--verbose', action='store_true', help='Set the flag,'
                                                                     ' if you want for results to be printed')
    parser.add_argument('-on', '--startontime', action='store_true', help='Set the flag, collecting data start'
                                                                          ' on the hour or on the min')

    args = parser.parse_args()

    config = Config.from_file(args.file, encoding='utf-8') if args.file else Config()
    config.use_stdoutwriter = config.use_stdoutwriter if config.use_stdoutwriter else False
    config.use_csvwriter = config.use_csvwriter if config.use_csvwriter else False
    config.start_on_time = config.start_on_time if config.start_on_time else False
    config.interval = config.interval if config.interval else 1
    config.timeunit = config.timeunit if config.timeunit else Timeunit.MIN

    config.use_stdoutwriter = True if args.verbose else config.use_stdoutwriter
    config.use_csvwriter = True if args.csvout else config.use_csvwriter
    config.start_on_time = True if args.startontime else config.start_on_time
    config.interval = args.interval if args.interval else config.interval
    config.timeunit = Timeunit.from_str(args.timeunit) if args.timeunit else config.timeunit

    out_repos: [Writer] = []
    if config.use_stdoutwriter:
        out_repos.append(StdOutWriter())

    if config.use_csvwriter:
        out_repos.append(CSVWriter(config.csvwriter_outpath))

    assert len(out_repos) > 0

    datasource = HtmlParseDataSource()
    nart = Nart(out_repos, datasource)

    if config.timeunit == Timeunit.HOUR:
        nart.run_with_hour(interval=config.interval, start_on_the_hour=config.start_on_time)
    elif config.timeunit == Timeunit.MIN:
        nart.run_with_min(interval=config.interval, start_on_the_min=config.start_on_time)
    elif config.timeunit == Timeunit.SEC:
        nart.run_with_sec(interval=config.interval)


if __name__ == "__main__":
    main()
