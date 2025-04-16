
import logging
import logging.config
import logging_info

class LoggingConfigDemo():

    def testlog(self):
        # set logging.conf file so it can be accessed
        logging.config.fileConfig("logging.conf")
        # create logger
        logger = logging.getLogger(LoggingConfigDemo.__name__)



        logging.info("info message")
        logging.warning("warning message")
        logging.critical("Critical message")


ll = LoggingConfigDemo()
ll.testlog()












