# -*- coding: utf-8 -*-
import scrapy
from wxspider import WxSpider
_spider_name='bdqn'

class BDQNSpider(WxSpider):  
    name=_spider_name
    def __init__(self, *args, **kwargs):
        super(BDQNSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://weixin.sogou.com/gzh?openid=oIWsFt2E6IQl_VQ1bSC8Z1o18tWA']
    
    def _extract_editor(self, sel, item):
        try:
            m=re.search(r'微信编辑(.*)',item['content'])
            editor=m.group(1)
        except:
            editor="NoBody"
        item['editor']=editor
        
    def _extract_author(self, sel, item):
        item['author']='北大青年'
        
def main():
    scrapy.cmdline.execute(argv = ['scrapy', 'crawl', _spider_name])

if __name__ == '__main__':
    main()