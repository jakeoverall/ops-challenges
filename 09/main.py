import logging
from logging import error
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

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
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt='%Y-%m-%dT%H:%M:%S')


def main():
    for i in range(100000):
        try:
            if(i % 3 == 0 and i % 5 == 0):
                logging.critical(f"{i}-FIZZBUZZ 🌟")
            elif(i % 3 == 0):
                logging.info(f"{i}-FIZZ")
            elif(i % 5 == 0):
                logging.warning(f"{i}-BUZZ")
            else:
                logging.debug(i)
        except Exception as err:
            logging.error(err)


if __name__ == "__main__":
    main()
