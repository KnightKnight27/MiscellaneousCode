# Cron parser -- Python tool for parsing cron strings

## Prerequisites
Python 3.7 is required to run this code. It may run on other 3.X versions, but has only
been tested on 3.7

## Installation
No installation needed other than Python 3.7 to run this. The `requirements.txt` file 
can be used to install dependencies for use in development e.g. `mypy`, `flake8` and `pytest`.
If you wish to install these run the following command

``python -m pip install -r requirements.txt``

## Instructions to run
Code can be run in place with the following command

``python cron_parser/parser.py INPUT_CRON_STRING ``

### For example running this command
``python cron_parser/parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"``

### gives the output
```minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Running tests
Install the dev dependencies and then use pytest to run the tests 
from the top-level `cron_parser` directory:

```pytest .```

## Check for invalid formatting and type errors
This can be done using the `flake8` and `mypy` tools repectively

`flake8 cron_parser test`

`mypy cron_parser test`
