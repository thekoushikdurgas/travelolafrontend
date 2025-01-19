
from utils.logger import logger

def filter_and_log_message(message: str, level: str = 'info'):
    """ Filter and log messages consistently. """
    message = message.strip()
    if level.lower() == 'debug':
        logger.debug(message)
    elif level.lower() == 'info':
        logger.info(message)
    elif level.lower() == 'warning':
        logger.warning(message)
    elif level.lower() == 'error':
        logger.error(message)
    else:
        logger.info(message)

    return message
