# nart
[![PyPI version shields.io](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.org/project/nart/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.org/project/nart/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

NART: NAver RealTime keywords

# Install
```console
foo@bar:~$ pip install --upgrade nart
```

# API
```python
from nart.nart import Nart
from nart.out.builtins.outcsvrepository import OutCsvRepository

outrepos = [OutCsvRepository(outpath='/tmp/test.csv')]
nart = Nart(outrepos)
nart.write_nart_to_repos()
nart.run_with_hour(interval=1)

```

You can define custom outrepositories and datasources by using inheriting OutRepository and DataSource

# Console
```console
usage: nart [-h] [-iv INTERVAL] [-csv CSVOUT] [-v] [-on] timeunit

NART needs arguments

positional arguments:
  timeunit              Input schedule time unit. (hour, min, or sec)

optional arguments:
  -h, --help            show this help message and exit
  -iv INTERVAL, --interval INTERVAL
                        Inverval time between collecting realtime keywords.
                        Timeunit is based on timeunit
  -csv CSVOUT, --csvout CSVOUT
                        Set the csvfilepath, if you want to write csvfile
  -v, --verbose         Set the flag, if you want for results to be printed
  -on, --startontime    Set the flag, collecting data start on the hour or on
                        the min
```

For example
```console
foo@bar:~$ nart sec -csv /tmp/test.csv -v -iv 1
```
