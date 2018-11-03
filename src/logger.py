import logging
import os
from time import strftime, localtime
from pathlib import Path

# To prevent dependencies on the STL's logging library keep these in this module
NOTSET = logging.NOTSET
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL


# TODO: Refactor to use pathlib
# TODO: Change to use log config file
# TODO: Add option to write to directories, e.g. log/logs/log0003_

DEFAULT_LOG_LOC = os.path.normpath('log')

consoles = {}


def console(name, level=NOTSET):
    if name in consoles:
        return consoles[name]
    logging_console = logging.StreamHandler()
    logging_console.setLevel(level)
    consoles[name] = logging_console
    return logging_console


def listen_to_log(target, handler):
    logging.getLogger(target).addHandler(handler)


def log(name, console_logging=False, level=NOTSET, log_folder=DEFAULT_LOG_LOC,
        log_format='%(asctime)s %(name)-12s %(levelname)-12s %(message)s', time_format='%Y-%m-%d %H,%M,%S'):

    log_start_time = strftime(time_format, localtime())
    log_folder = os.path.normpath(log_folder)
    log_file_name = '{log_name} {time}.log'.format(log_name=name, time=log_start_time)
    log_file = os.path.join(log_folder, log_file_name)

    # Create log file
    Path.mkdir(Path(log_folder), exist_ok=True)
    Path.touch(Path(log_file))

    # Get logger and set formatting
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger_format = logging.Formatter(fmt=log_format, datefmt=time_format)

    # Configure logging to file
    log_file_handler = logging.FileHandler(log_file)
    log_file_handler.setLevel(level)
    log_file_handler.setFormatter(logger_format)
    logger.addHandler(log_file_handler)

    # Add console as logging handler
    if console_logging:
        logger.addHandler(console(name, level))

    return logger
