from use_log import basicUse
from log import Log_me

logger = Log_me(log_file='test_logging_new.log', log_dir='.')

logger.info('this will log into another file')
logger.debug('this will log into another file')
logger.warn('this will log into another file')

basicUse()

logger.error('this will log into another file')
