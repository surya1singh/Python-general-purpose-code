#import sys
import os
import logging
import logging.handlers
import inspect

MaxBytes=10240000
BackupCount=100
#scriptdir = sys.path[0]
#log_dir = scriptdir + '/logs'

""" Simple Logging Class """
class Log_me:
    """ __init__ method:: Open a log files and writes log with respect to module and logging level"""
    def __init__(self,*args,**kargs):
        try:
            self.log_dir=kargs["log_dir"]
            log_file=args[0]
            self.log_filename=self.log_dir+'/'+log_file
#            self.log_dir=os.path.split(self.log_filename)[0]
            self.frame,self.filename,self.line_number,self.function_name,self.lines,self.index=inspect.getouterframes(inspect.currentframe())[1]
            self.filename=os.path.basename(self.filename)
            if not os.path.isdir(self.log_dir):
                os.makedirs(self.log_dir)
                os.chmod(self.log_dir,0777)
            LOG_FILENAME=self.log_filename
            self.logger=logging.getLogger(self.filename)
            self.logger.setLevel(logging.DEBUG)
            self.handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=MaxBytes, backupCount=BackupCount)
            formatter = logging.Formatter("%(asctime)s - %(name)s - (%(threadName)-10s) - %(levelname)s - %(message)s",datefmt='%Y-%m-%d %H:%M:%S')
            self.handler.setFormatter(formatter)
            self.logger.addHandler(self.handler)
        except Exception,e:
            print('error during Log_me.__init__ :: %s'%str(e))

    """ info """
    def info(self,log_data):
        try:
            self.logger.info(log_data)
        except Exception, e:
            print(e)

    """ error """
    def error(self,log_data):
        try:
            self.logger.error(" function_name:"+self.function_name+": "+log_data)
        except Exception, e:
            print(e)

    """ warn """
    def warn(self,log_data):
        try:
            self.logger.warn(log_data)
        except Exception, e:
            print(e)

    """ critical """
    def critical(self,log_data):
        try:
            self.logger.critical(" function_name:"+self.function_name+": "+log_data)
        except Exception, e:
            print(e)

    """ shutdown:: close and remove the handler and shuts down the logger instance. """
    def shutdown(self):
        try:
            self.handler.close()
            self.logger.removeHandler(self.handler)
            logging.shutdown()
        except Exception, e:
            print(e)
