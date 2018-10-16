import logging, os
from time import strftime, localtime
from pathlib import Path

# TODO: Change to use log config file
# TODO: Add option to write to directories, e.g. log/logs/log0003_

DEFAULT_LOG_LOC = os.path.normpath('log')


def get(log_name,
        console_logging=False, level=logging.DEBUG, log_loc=DEFAULT_LOG_LOC,
        log_fmt='%(asctime)s %(name)-12s %(levelname)-12s %(message)s', time_fmt='%Y-%m-%d %H,%M,%S'):

    log_loc = os.path.normpath(log_loc)
    log_start_time = strftime(time_fmt, localtime())
    log_file_name = '{log_name} {time}.log'.format(log_name=log_name, time=log_start_time)

    log_file = os.path.join(log_loc, log_file_name)

    # Create log file if needed
    open(log_file, 'a').close()

    # Get logger and set formatting
    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    fmt = logging.Formatter(fmt=log_fmt, datefmt=time_fmt)

    # Configure logging to file
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    # Add console as logging handler
    if console_logging:
        console = logging.StreamHandler()
        console.setLevel(level)
        logger.addHandler(console)  # Add console as handler to root logger

    return logger

# In the future a listen function will allow passed handlers to listen to to loggers
