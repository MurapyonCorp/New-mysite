"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging
import logtest

logging.basicConfig(level = logging.INFO)

logging.info('info')

logtest.do_something()