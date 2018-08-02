import logging

class Log_me ():
    def __init__(self,**kwargs):
        pass

    def info(self,log_data):
        """ info """
        try:
            self.logger.info(log_data)
        except Exception, e:
            print(e)

    def error(self,log_data):
        """ error """
        try:
            self.logger.error(" function_name:"+self.function_name+": "+log_data)
        except Exception, e:
            print(e)

    def warn(self,log_data):
        """ warn """
        try:
            self.logger.warn(log_data)
        except Exception, e:
            print(e)

    def critical(self,log_data):
        """ critical """
        try:
            self.logger.critical(" function_name:"+self.function_name+": "+log_data)
        except Exception, e:
            print(e)

    def shutdown(self):
        """ shutdown:: close and remove the handler and shuts down the logger instance. """
        try:
            self.handler.close()
            self.logger.removeHandler(self.handler)
            logging.shutdown()
        except Exception, e:
            print(e)
