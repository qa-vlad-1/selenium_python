import logging

class loggingDemoConsole():

    def testlog(self):

        # define logger
        logger = logging.getLogger("sampleLog")
        # set Level of Logging
        logger.setLevel(level=logging.INFO)

        # define console handler
        # log error to SteramHandler (Console)
        c_handler = logging.StreamHandler()
        # Set level of logging on StreamHandler()/Console
        c_handler.setLevel(level=logging.INFO)

        # Transfer logging to Formatter
        # define how you want to format logs
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Add formatter to Console Handler - c_handler
        c_handler.setFormatter(formatter)

        # Add console handler - c_handler to Logger
        logger.addHandler(c_handler)

        # Log messages
        logger.info("INFO message logged")
        logger.error("Error message logged")
        logger.warning("Warning message logged")
        logger.critical("Critical message logged")


ll = loggingDemoConsole()
ll.testlog()











