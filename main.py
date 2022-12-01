from sensor.logger import logging
from sensor.exception import sensorException

def test_logger_and_exception():
     try:
          logging.info("starting the test logger and exception")
          result=3/10
          print(result)
          logging.info("stopping the test logger and exception")
          pass
     except Exception as e:
          logging.debug("stopping the test_logger and exception")
          raise sensorException(e, sys)

if __name__== "__main__":
     try:
          pass
     except Exception as e:
          print(e)