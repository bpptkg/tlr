#!/usr/bin/env python

import logging
import logging.config
import os
import sys

from tlr.app import App
from tlr.settings import LOCKFILE, LOGGING

logger = logging.getLogger(__name__)

if sys.version_info < (3, 6):
    sys.exit('Error: tlr requires Python 3.6 or above')


def run_from_command_line():
    logging.config.dictConfig(LOGGING)

    try:
        app = App(lockfile=LOCKFILE)
        app.run()
    except (ConnectionError, OSError) as e:
        # Pass connection error and no route to host error. Log on debug only.
        logger.debug(e)
        pass
    except Exception as e:
        logger.error(e)
        raise e

    os.execv(__file__, sys.argv)


if __name__ == '__main__':
    try:
        run_from_command_line()
    except KeyboardInterrupt:
        pass
