import multiprocessing
import queue
import logging
from logging.handlers import QueueHandler, QueueListener


def main():
    q = queue.Queue
    queue_handler = QueueHandler(q)
    handler = logging.StreamHandler()
    listener = QueueListener(q, handler)
    root = logging.getLogger()
    root.addHandler(queue_handler)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    handler.setFormatter(formatter)
    listener.start()


if __name__ == '__main__':
    main()


