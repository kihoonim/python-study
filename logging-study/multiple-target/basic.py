import logging
import time
import threading


def create_logger():
    

    formatter1 = logging.Formatter(
        'format1 %(relativeCreated)6d %(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s')
  
    formatter2 = logging.Formatter(
        'format2 %(relativeCreated)6d %(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s')
  
    formatter3 = logging.Formatter(
        'format3 %(relativeCreated)6d %(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s')
  

    ch1 = logging.StreamHandler()
    ch1.setLevel(logging.DEBUG)

    ch2 = logging.StreamHandler()
    ch2.setLevel(logging.DEBUG)
    
    ch3 = logging.StreamHandler()
    ch3.setLevel(logging.DEBUG)

    ch1.setFormatter(formatter1)
    ch2.setFormatter(formatter2)
    ch3.setFormatter(formatter3)

    logger1 = logging.getLogger('logger1')
    logger1.setLevel(logging.DEBUG)

    logger2 = logging.getLogger('logger2')
    logger2.setLevel(logging.DEBUG)

    logger3 = logging.getLogger('logger3')
    logger3.setLevel(logging.DEBUG)
    
    logger1.addHandler(ch1)
    logger2.addHandler(ch2)
    logger3.addHandler(ch3)


def main():
    create_logger()
    logger1 = logging.getLogger('logger1')
    logger2 = logging.getLogger('logger2')
    logger3 = logging.getLogger('logger3')

    logger1.info('hello')
    logger2.info('hello')
    logger3.info('hello')

    logger1.warning('hello')
    logger2.warning('hello')
    logger3.warning('hello')


if __name__ == '__main__':
    main()


