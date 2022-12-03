from sensor.logger import logging
from sensor.exception import SensorException

def test_logger_and_exception():
     try:
          logging.info("starting the test logger and exception")
          result=3/0
          print(result)
          logging.info("stopping the test logger and exception")
          pass
     except Exception as e:
          logging.debug("stopping the test_logger and exception")
          raise sensorException(e, sys)

if __name__== "__main__":
     try:
          test_logger_and_exception()
     except Exception as e:
          print(e)