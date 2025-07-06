import logging
import sys
from logging.handlers import RotatingFileHandler
from watchtower import CloudWatchLogHandler

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Local file handler
    file_handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=2)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # CloudWatch handler
    try:
        cw_handler = CloudWatchLogHandler(log_group='fastapi-microservice-logs')
        cw_handler.setLevel(logging.INFO)
        cw_handler.setFormatter(formatter)
        logger.addHandler(cw_handler)
    except Exception as e:
        logger.error(f"CloudWatch logging setup failed: {e}")

    # Stream handler for console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
