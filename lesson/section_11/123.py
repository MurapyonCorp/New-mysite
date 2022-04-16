import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('New-mysite/lesson/section_11/logtest.log')
logger.addHandler(h)

def do_something():
  logger.info('from logtest')
  logger.debug('from logtest debug')