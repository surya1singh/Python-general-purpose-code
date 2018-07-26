try:
    import MySQLdb
except:
    import mysql.connector as MySQLdb

import traceback
import os
import re
import time


""" Db Class """
class Db:
    """ __init__ method """
    def __init__(self,*args,**kargs):
        self.logger=kargs["log"]
        try:
            mysql_credentials=args[0]
            if(len(args)>1):
                self.error_file_path=args[1]
            self.remote_host=mysql_credentials[0]
            self.mysql_host= mysql_credentials[1]
            self.mysql_port_list= mysql_credentials[2].split('|')
            self.mysql_un= mysql_credentials[3]
            self.mysql_pw= mysql_credentials[4]
            self.dbase= mysql_credentials[5]
            conn_flag=0
            if self.remote_host.lower()=="y" and self.mysql_host<>'localhost':
                self.logger.info('connection would be made for every query')
            else:
                for mysql_port in self.mysql_port_list:
                   attempts=0;
                   while(attempts<2):
                    try:
                        self.logger.info('connecting with database %s'%self.dbase)
                        self.conn = MySQLdb.connect(host=self.mysql_host,port=int(mysql_port),\
                        user=self.mysql_un,passwd=self.mysql_pw,db=self.dbase)
                        if self.conn:
                            self.logger.info('connection with database %s successful'%self.dbase)
                            conn_flag=1
                            break

                    except Exception,e:
                        self.logger.error('Exception connecting to db %s : %s'%(self.dbase,str(e)))
                        attempts=attempts+1
                        if(attempts<2):
                           self.logger.info('going to sleep, re-try after 2 mins')
                           time.sleep(120)
                   if(conn_flag==1):
                              break
                if(conn_flag==0):
                        file=self.error_file_path+'/mysql_eror.txt'
                        f=open(file,'w')
                        f.writelines("Error while connecting to MySql")
                        f.close()


        except Exception:
            self.logger.error('Traceback of exception during Db.__init__: %s'%traceback.format_exc())

    """ function to close database and exit system """
    def close_conn(self):
        try:
            if self.remote_host.lower()=="y" and self.mysql_host<>'localhost':
                pass
            else:
                self.logger.info('closing db connection')
                self.conn.close()
        except Exception:
            self.logger.error('Traceback of exception during Db.close_conn :: %s'%traceback.format_exc())

    """ function to execute and commit mysql query """
    def fun_execute_query(self,query):
        try:
            if self.remote_host.lower()=="y" and self.mysql_host<>'localhost':
                for mysql_port in self.mysql_port_list:
                    cmd='mysql -h%s -P%d -u%s -p%s --database=%s -e"%s;"'%(self.mysql_host,int(mysql_port),self.mysql_un,\
                    self.mysql_pw,self.dbase,query)
                    self.logger.info('cmd :: ' + cmd )
                    resultset=os.popen(cmd).readlines()
                    if resultset:
                        self.mysql_port_list=[mysql_port]
                        break
            else:
                try:
                    cursor = self.conn.cursor()
                    self.logger.info(str(query))
                    cursor.execute(query)
                    #resultset = cursor.fetchall()
                    self.conn.commit()
                    cursor.close()
                except MySQLdb.IntegrityError, e:
                    self.logger.error('Query Execution failed with exception : %s'%str(e))
                    return []
                except MySQLdb.Error, e:
                    self.logger.error('Query Execution failed with exception : %s'%str(e))
                    error=str(e)
                    error=error.replace(error[1:7],'')
                    if(str(e).find('Table')==-1):
                          self.logger.info("fetching table name")
                          table_name=query[query.find('from')+5:query.find(' ',query.find('from')+6)]
                          self.logger.info(error)
                          if(error.find('field list')<>-1):
                                        self.logger.info('appending table name')
                                        error=error.replace("'field list","table '%s"%table_name)
                                        self.logger.info(error)
                    file=self.error_file_path+'/db_error.txt'
                    curr_time = time.strftime('%Y%m%d%H%M%S')
                    f=open(file,'a')
                    f.writelines("%s:%s\n"%(str(curr_time),error))
                    f.close()

                    return []
                except MySQLdb.Warning, e:
                    self.logger.info('Query Execution succeed with warning : %s'%str(e))
            return resultset
        except Exception:
             self.logger.error('Traceback of exception during Db.fun_execute_query :: %s'%traceback.format_exc())
             return []

    """ to run query on remote server and writing the result on file """
    def outfile_processing(self,column_list,file_name,enclosed_by,terminated_by,escaped_by,from_table,where_condition,custom_query=None):
        try:
#            delete outfile if already exists
            if where_condition:
		if custom_query and custom_query.__contains__(' where '):where_condition='and %s'%where_condition
		else:where_condition='where %s'%where_condition
            if self.remote_host.lower()=="y" and self.mysql_host<>'localhost':
		if custom_query:query="%s %s into outfile '%s' fields terminated by '%s' optionally enclosed by '%s' escaped by '%s' lines terminated by '\\n'"%(custom_query,where_condition,file_name,terminated_by,enclosed_by, escaped_by)
                else:query="select sql_no_cache %s from %s %s"%(column_list,from_table,where_condition)
                self.logger.info(query)
                resultset=self.fun_execute_query(query)
                if resultset:
                    resultset.remove(resultset[0])
                    file=open(file_name,'w')
                    for line in resultset:
                        file.write(re.sub('^|$','%s'%enclosed_by,re.sub('\\t','%s%s%s'%(enclosed_by,terminated_by,enclosed_by)\
                        ,re.sub('\\n','',line)))+"\n")
                    file.close()
            else:
		if custom_query:query="%s %s into outfile '%s' fields terminated by '%s' optionally enclosed by '%s' escaped by '%s' lines terminated by '\\n'"%(custom_query,where_condition,file_name,terminated_by,enclosed_by,escaped_by)
                else:
					query = "select sql_no_cache %s into outfile '%s' fields terminated by '%s' \
                optionally enclosed by '%s' escaped by '%s' lines terminated by '\\n' from %s %s"\
                %(column_list,file_name,terminated_by,enclosed_by,escaped_by,from_table,where_condition)
		self.logger.info(query)
                self.fun_execute_query(query)

            return 1
        except Exception,e:

            self.logger.error('Exception during remote_db_processing :: %s'%str(e))
            return 0
