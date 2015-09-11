# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class WxSpiderMySQLPipeline(object):
    host='localhost'
    user='root'
    passwd='admin'
    db='wx_article'
    charset='utf8'
    def __init__(self):
        self.db=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.cursor = self.db.cursor()
        
    def process_item(self, item, spider):
        sql="INSERT INTO %s"%spider.name
        sql+="(mid,title,des,content,time,author,url,editor,html) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,(item['mid'],item['title'],item['des'],item['content'],item['time'],item['author'],item['url'],item['editor'],item['html']))
            self.db.commit()
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            if e.args[0]==1062:
                return item
        return item
