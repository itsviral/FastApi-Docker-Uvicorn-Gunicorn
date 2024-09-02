import logging
from logging.handlers import TimedRotatingFileHandler
from uvicorn.logging import DefaultFormatter

def get_logger(name):
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a formatter for log messages
    formatter = DefaultFormatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    # Stream handler for outputting logs to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # File handler for rotating logs every day
    file_handler = TimedRotatingFileHandler('app/logs/app.log', when='midnight', interval=1, backupCount=60)
    file_handler.suffix = '%Y%m%d'
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Separate handler for Uvicorn access logs
    access_log_handler = TimedRotatingFileHandler('app/logs/app.log', when='midnight', interval=1, backupCount=60)
    access_log_handler.suffix = '%Y%m%d'
    access_log_handler.setLevel(logging.INFO)
    access_log_handler.setFormatter(formatter)

    # Attach the handler to Uvicorn's access logger
    uvicorn_logger = logging.getLogger('uvicorn.access')
    uvicorn_logger.addHandler(access_log_handler)

    return logger
