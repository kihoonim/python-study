import logging
import logging.config


def create_logger():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('example')
    return logger


def main():
    logger = create_logger()
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


