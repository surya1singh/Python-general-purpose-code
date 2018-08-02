from log import Log_me


def basicUse():
    logger = Log_me(log_file='test_logging.log', log_dir='.')
    logger.debug('This is debug info')
    logger.info('This is info info')
    logger.warn('This is warning info')
    logger.error('This is error info')
    logger.critical('This is critical info')



if __name__ == '__main__':
    basicUse()
