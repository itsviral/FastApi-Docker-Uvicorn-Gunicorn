import logging
from logging.handlers import TimedRotatingFileHandler
from uvicorn.logging import DefaultFormatter

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create a formatter that specifies the log message's format
    formatter = DefaultFormatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    # create a StreamHandler that sends log messages to standard output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    logger.addHandler(stream_handler)

    # set up a TimedRotatingFileHandler that rotates every day for the main log file
    file_handler = TimedRotatingFileHandler('app/logs/app.log', when='midnight', interval=1, backupCount=60)
    file_handler.suffix = '%Y%m%d'
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # set up a separate file handler for Uvicorn access logs
    access_log_handler = TimedRotatingFileHandler('app/logs/app.log', when='midnight', interval=1, backupCount=60)
    access_log_handler.suffix = '%Y%m%d'
    access_log_handler.setLevel(logging.INFO)
    access_log_handler.setFormatter(formatter)

    # capture Uvicorn access logs in the separate file
    uvicorn_logger = logging.getLogger('uvicorn.access')
    uvicorn_logger.addHandler(access_log_handler)

    return logger
