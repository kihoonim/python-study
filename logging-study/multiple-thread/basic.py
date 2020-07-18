import logging
import time
import threading


def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(relativeCreated)6d %(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger


def worker(logger):
    for i in range(5):
        logger.debug('Debug Message')
        logger.info('Info Message')
        logger.warning('Warning Message')
        logger.error('Error Message')
        logger.critical('Critical Message')

        time.sleep(3)


def main():
    logger = create_logger('example')
    thread = threading.Thread(target=worker, args=(logger,))
    thread.start()
    thread.join()
    


if __name__ == '__main__':
    main()


