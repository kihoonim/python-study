import logging

def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fh = logging.handlers.TimedRotatingFileHandler(
        filename='log.log',
        backupCount=5, 
        when='midnight'
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    
    return logger


def main():
    logger = create_logger('example')
    logger.debug('Debug Message')
    logger.info('Info Message')
    logger.warning('Warning Message')
    logger.error('Error Message')
    logger.critical('Critical Message')

    logging.debug('Debug Message')
    logging.info('Info Message')
    logging.warning('Warning Message')
    logging.error('Error Message')
    logging.critical('Critical Message')


if __name__ == '__main__':
    main()


