# -*- coding: utf-8 -*-
import scrapy
from wxspider import WxSpider
_spider_name='gzh'

class GZHSpider(WxSpider):  
    name=_spider_name
    def __init__(self, *args, **kwargs):
        super(GZHSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://weixin.sogou.com/gzh?openid=oIWsFt6Umaa8FoZzzcl8evF8HG7E']
    
    def _extract_editor(self, sel, item):
        item['editor']='NoBody'
        
    def _extract_author(self, sel, item):
        item['author']='光之华'

def main():
    scrapy.cmdline.execute(argv = ['scrapy', 'crawl', _spider_name])

if __name__ == '__main__':
    main()