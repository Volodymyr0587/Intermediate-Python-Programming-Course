import logging
import logging.config
import os
import sys  # needed for sys.stdout in config
import time
import traceback
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Get absolute path to logging.conf relative to this script
""" config_path = os.path.join(os.path.dirname(__file__), 'logging.conf')


logging.config.fileConfig(config_path)

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message') """


""" try:
    a = [1, 2, 3]
    val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)
except:
    logging.error("The error is %s", traceback.format_exc()) """
    
    
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
# log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')
# handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)

log_file_path = os.path.join(os.path.dirname(__file__), 'timed_test.log')
handler = TimedRotatingFileHandler(log_file_path, when='s', interval=5, backupCount=5)

logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('Hello, world!')


for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)
