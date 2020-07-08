#!/usr/bin/env python

import logging
import logging.config
import os
import sys
import time

from tlr import app, settings

logger = logging.getLogger(__name__)

if sys.version_info < (3, 6):
    sys.exit('Error: tlr requires Python 3.6 or above')


def run_from_command_line():
    logging.config.dictConfig(settings.LOGGING)

    try:
        tlr_app = app.App(lockfile=settings.LOCKFILE)
        tlr_app.run()
    except (ConnectionError, OSError) as e:
        # Pass connection error and no route to host error. Log on debug only.
        logger.debug(e)

        # Sleep for a while before reconnecting.
        logger.debug('Sleeping for a while before reconnecting...')
        time.sleep(settings.TELNET_RECONNECT_TIMEOUT)
    except Exception as e:
        logger.error(e)
        raise e

    os.execv(__file__, sys.argv)


if __name__ == '__main__':
    try:
        run_from_command_line()
    except KeyboardInterrupt:
        pass
