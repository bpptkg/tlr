#!/usr/bin/env python

import logging
import logging.config
import os
import sys

from tlr.app import main
from tlr.settings import LOGGING

logger = logging.getLogger(__name__)

if sys.version_info < (3, 6):
    sys.exit('Error: tlr requires Python 3.6 or above')


def run_from_command_line():
    logging.config.dictConfig(LOGGING)

    try:
        main()
    except Exception as e:
        logger.error(e)
        raise e

    os.execv(__file__, sys.argv)


if __name__ == '__main__':
    run_from_command_line()
