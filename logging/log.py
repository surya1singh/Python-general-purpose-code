import inspect
import logging
import os
import traceback

MaxBytes = 1024*1024
BackupCount = 10

class Log_me():
    def __init__(self,**kwargs):
        self.log_dir = kargs["log_dir"]
        self.filename = kargs["log_file"]
        self.log_filename = self.log_dir + '/' + self.filename
        self.frame, self.filename,self.line_number,self.function_name,self.lines,self.index = inspect.getouterframes(inspect.currentframe())[1]
        if not os.path.isdir(self.log_dir):
            os.makedirs(self.log_dir)
            os.chmod(self.log_dir,0777)
        self.logger = logging.getLogger(self.filename)
        self.logger.setLevel(logging.DEBUG)
        self.addHandler()

    def addHandler(self):
        """ add handler """
        self.handler = logging.handlers.RotatingFileHandler(self.log_filename, maxBytes=MaxBytes, backupCount=BackupCount)
        formatter = logging.Formatter("%(asctime)s - %(name)s - (%(threadName)-10s) - %(levelname)s - %(message)s",datefmt='%Y-%m-%d %H:%M:%S')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

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
