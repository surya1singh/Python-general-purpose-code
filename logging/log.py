import logging
import logging.handlers
import os
import traceback

MaxBytes = 1024*1024
BackupCount = 10

class Log_me():
    def __init__(self,**kwargs):
        self.log_dir = kwargs["log_dir"]
        self.filename = kwargs["log_file"]
        self.log_filename = self.log_dir + '/' + self.filename
        if not os.path.isdir(self.log_dir):
            os.makedirs(self.log_dir)
            os.chmod(self.log_dir,777)
        self.logger = logging.getLogger(self.filename)
        self.logger.setLevel(logging.DEBUG)
        self.addHandler()

    def addHandler(self):
        """ add handler """
        self.handler = logging.handlers.RotatingFileHandler(self.log_filename, maxBytes=MaxBytes, backupCount=BackupCount)
        formatter = logging.Formatter("%(asctime)s - %(name)s - (%(threadName)-10s) - %(levelname)s - %(message)s",datefmt='%Y-%m-%d %H:%M:%S')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def debug(self,log_data):
        """ info """
        try:
            self.logger.debug(log_data)
        except Exception:
            print(traceback.format_exc())

    def info(self,log_data):
        """ info """
        try:
            self.logger.info(log_data)
        except Exception:
            print(traceback.format_exc())

    def error(self,log_data):
        """ error """
        try:
            self.logger.error(log_data)
        except Exception:
            print(traceback.format_exc())

    def warn(self,log_data):
        """ warn """
        try:
            self.logger.warn(log_data)
        except Exception:
            print(traceback.format_exc())

    def critical(self,log_data):
        """ critical """
        try:
            self.logger.critical(log_data)
        except Exception:
            print(traceback.format_exc())

    def shutdown(self):
        """ shutdown:: close and remove the handler and shuts down the logger instance. """
        try:
            self.handler.close()
            self.logger.removeHandler(self.handler)
            logging.shutdown()
        except Exception:
            print(traceback.format_exc())
