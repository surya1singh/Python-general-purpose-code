import BeautifulSoup
import urllib
import db
import xml.dom.minidom
import log
import sys

path = sys.path[0]

config_file = path+'/config.xml'
log_file = 'log.txt'

logger = log.Log_me(log_file,log_dir=path+'/logs')


def read_config():
    doc = xml.dom.minidom.parse(config_file)
    for data in doc.getElementsByTagName("data"):
        depth = int(data.getAttribute("depth"))
        host = data.getAttribute("host")
        remote_host = data.getAttribute("remote_host")
        port = data.getAttribute("port")
        db_user = data.getAttribute("db_user")
        db_pass = data.getAttribute("db_pass")
        db_name = data.getAttribute("db")
        url = data.getAttribute("url")
        query = data.getAttribute("query")
        mysql_credentials = [remote_host,host,port,db_user,db_pass,db_name]
    return mysql_credentials,depth,url,query



mysql_credentials,depth,url,query = read_config()

query_list = [query+str(x) for x in range(depth)]

local_db = db.Db(mysql_credentials,path,log=logger)


def get_page_generator(address='', query=[]):
    for p in query:
        website = urllib.urlopen(address+p)
        data = website.read()
        website.close()
        yield data

def return_tag_details(soup,tag='',value=('class','storylink')):
    all_tag = soup.findAll(tag,attrs={value[0]:value[1]})
    return all_tag


def get_news():
    page=get_page_generator(address=url,query=query_list)
    for p in page:
        soup = BeautifulSoup.BeautifulSoup(p)
        for table_row in return_tag_details(soup.body,tag='tr', value=['class','athing']):
            try:
                for attr,val in table_row.attrs:
                    if attr == 'id':
                        data_id = val
                else:
                    #td_data = return_tag_details(table_row, tag='td', value=['class','votelinks'])
                    #a_data = return_tag_details(td_data[0], tag='a',value=('class',None))
                    #data_id = a_data[0].attrs[0]
                    #data_id = data_id[1].split('_')[-1]
                    for table_data in return_tag_details(table_row,tag='td', value=['class','title']):
                        for anchor_data in return_tag_details(table_data,'a'):
                            link=anchor_data.attrs[0][-1]
                            if link.startswith('http'):
                                title = anchor_data.text
                                url_link = link
                                insert_query = "insert into news_details (id,url,title) values('%s','%s','%s') ON DUPLICATE KEY UPDATE votes=votes+1 " %(data_id,url_link,title)
                                result = local_db.fun_execute_query(insert_query)
            except:
                raise

if __name__=='__main__':
    get_news()
