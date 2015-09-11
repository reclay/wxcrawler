# -*- coding: utf-8 -*-
import scrapy
from wxspider import WxSpider
_spider_name='xf'

class XfSpider(WxSpider):  
    name=_spider_name
    def __init__(self, *args, **kwargs):
        super(XfSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://weixin.sogou.com/gzh?openid=oIWsFt1mdY_3guZraCVTSTqnE5U0']
    def _extract_editor(self, sel, item):
        author=sel.xpath('//*[contains(@class,"rich_media_meta")]/text()').extract()
        author=''.join([x.strip() for x in author])
        author=author[10:-2]
        item['author']=author
        
    def _extract_author(self, sel, item):
        try:
            m=re.search(r'责任编辑：?(.*)',item['content'])
            editor=m.group(1)
        except:
            editor="NoBody"
        item['editor']=editor
def main():
    scrapy.cmdline.execute(argv = ['scrapy', 'crawl', _spider_name])

if __name__ == '__main__':
    main()