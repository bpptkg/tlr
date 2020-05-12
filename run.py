#!/usr/bin/env python

import logging
import os
import sys
from logging.config import dictConfig

from tlr.app import main
from tlr.settings import LOGGING

logger = logging.getLogger(__name__)

if sys.version_info < (3, 6):
    sys.exit('Error: tlr requires Python 3.6 or above')


def run_from_command_line():
    dictConfig(LOGGING)

    try:
        main()
    except Exception as e:
        logger.error(e)

    os.execv(__file__, sys.argv)


if __name__ == '__main__':
    run_from_command_line()
