"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

# logging.basicConfig(level = logging.DEBUG)
formattar = '%(asctime)s:%(message)s'
logging.basicConfig(level = logging.INFO, format = formattar)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

logging.info('info %s %s' % ('test', 'test2'))