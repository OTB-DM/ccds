import logging
import logging.handlers
import os

import colorlog


def get_logger(name):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    formatter = colorlog.ColoredFormatter(
        "%(white)s%(asctime)s - %(funcName)s - %(log_color)s%(levelname)-8s%(reset)s"
        "%(cyan)s%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red",
        },
    )
    logger.setLevel(logging.DEBUG)

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(os.path.join("logs", f"{name}.log"), encoding="utf-8")

    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    f_format = logging.Formatter(
        "%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    return logger
