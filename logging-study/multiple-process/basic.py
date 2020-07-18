import logging
import multiprocessing
from logging.handlers import QueueHandler, QueueListener


def create_log_listener(name, q):
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
        '%(relativeCreated)6d %(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # logger.addHandler(ch)
    # logger.addHandler(fh)

    listener = QueueListener(q, ch, fh)
    listener.start()


def create_log_writer(q):
    qh = QueueHandler(q)
    logger = logging.getLogger()
    logger.addHandler(qh)
    
    return logger



def worker():
    pass

def main():
    q = multiprocessing.Queue(-1)

    create_log_listener('logger1', q)

    p = multiprocessing.Process(
        target=worker, 
        name='worker 1',
        args=(q,))


if __name__ == '__main__':
    main()