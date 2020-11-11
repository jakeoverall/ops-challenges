import logging
from logging import error
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


logger = logging.getLogger(__name__)


def configure_logger():
    logging.basicConfig(
        handlers=[
            RotatingFileHandler(
                './s-log.log',
                delay=False,
                maxBytes=1000,
                backupCount=3
            ),
            TimedRotatingFileHandler(
                './t-log.log',
                when='S',
                interval=1,
                backupCount=4,
                delay=False
            )],
        level=logging.DEBUG,
        format="[%(asctime)s] %(name)s || %(levelname)s || %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('errors.log')
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'))
    file_handler.setLevel(logging.ERROR)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


def main():
    for i in range(1000):
        try:
            if(i % 3 == 0 and i % 5 == 0):
                logger.critical(f"{i}-FIZZBUZZ 🌟")
            elif(i % 3 == 0):
                logger.info(f"{i}-FIZZ")
            elif(i % 5 == 0):
                logger.warning(f"{i}-BUZZ")
            else:
                logger.debug(i)
        except Exception as err:
            logger.error(err)
    logger.error("EVERYTHING WORKED...")


if __name__ == "__main__":
    configure_logger()
    main()
