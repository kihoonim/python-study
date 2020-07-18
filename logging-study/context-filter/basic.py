import logging
from random import choice

class ContextFilter(logging.Filter):

    USERS = ['jim', 'fred', 'sheila']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

    def filter(self, record):
        record.ip = choice(ContextFilter.IPS)
        record.user = choice(ContextFilter.USERS)
        return True


def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)-15s %(name)-5s %(levelname)-8s IP: %(ip)-15s User: %(user)-8s %(message)s')

    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger


def main():
    logger1 = create_logger('a.b.c')
    logger2 = create_logger('d.e.f')

    f = ContextFilter()

    logger1.addFilter(f)
    logger2.addFilter(f)

    logger1.debug('Debug Message')
    logger1.info('Info Message')
    logger2.warning('Warning Message')
    logger2.error('Error Message')
    logger2.critical('Critical Message')


if __name__ == '__main__':
    main()