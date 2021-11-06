import logging
import sys


formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def get_test_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.WARN)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler("log.txt", "a+", "utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
