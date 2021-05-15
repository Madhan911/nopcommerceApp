import inspect
import logging


class LogGen:

    @staticmethod
    def loggingDmo():


        loggername = inspect.stack()[1][3]
        # getLogger() method takes the test case name as input
        logger = logging.getLogger(loggername)
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('.\\Logs\\logfile.log')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.INFO)
        return logger