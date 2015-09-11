# -*- coding: utf-8 -*-
import scrapy
from wx_spider.items import WxSpiderItem
from scrapy import Selector
import re,lxml
from selenium import webdriver
from time import sleep
from scrapy import log

class WxSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super(WxSpider, self).__init__(*args, **kwargs)
        self.start_urls = []

    def start_requests(self):
        # self.web=webdriver.PhantomJS(executable_path='/Users/Jackhuanghuang/Documents/pythonlearing/phantomjs/phantomjs')
        # self.web.get(self.start_urls[0])
        # more_ele=self.web.find_elements_by_xpath('//div[@id="wxmore"]/a')[0]
        # for i in range(7):
        #     sleep(5)
        #     more_ele.click()
        # self.web.save_screenshot('1.png')
        # f=file('tmp.txt','w')
        # f.write(self.web.page_source.encode('utf8'))
        with file('tmp.txt') as f:
            etree=lxml.html.fromstring(f.read())
        node=etree.xpath('//div[@class="txt-box"]//a/@href')
        for i in node:
            url='http://weixin.sogou.com'+i
            yield scrapy.Request(url,callback=self.parse_item)

    def parse_item(self, response):#get the item
        self.log('Parse Item link: %s' % response.url, log.DEBUG)
        sel = Selector(response)
        item = WxSpiderItem()
        # each spider overrides the following methods
        self._extract_url(sel,item)
        self._extract_mid(sel, item)
        self._extract_title(sel, item)
        self._extract_des(sel, item)
        self._extract_author(sel, item)
        self._extract_editor(sel, item)
        self._extract_html(sel, item)
        self._extract_content(sel,item)
        self._extract_time(sel, item)
        # auto filled methods, don't need to override them
        # must include the following methods if you override parse_item
        return item
    
    def _extract_url(self,sel,item):
        item['url']=sel.response.url

    def _extract_mid(self,sel,item):
        url=sel.response.url
        m=re.search(r'mid=(.*?)&.*idx=(.)',url)
        mid=m.group(1)+'idx'+m.group(2)
        item['mid']=mid

    def _extract_title(self,sel,item):
        title=sel.xpath('//title/text()').extract()[0]
        item['title']=title

    def _extract_des(self,sel,item):
        des0=sel.xpath('//script[@type="text/javascript"]/text()').extract()[-1]
        m=re.search(r'msg_desc.?=.?(?P<des>.*);',des0)
        des=m.groups('des')[0].encode('utf8')    
        item['des']=des

    def _extract_html(self,sel, item):
        item['html']=sel.response.body

    def _extract_content(self,sel,item):
        content=sel.xpath('//div[@class="rich_media_content"]//text()').extract()                
        content=''.join([x.strip() for x in content]).encode('utf8')
        item['content']=content

    def _extract_time(self,sel, item):
        time=sel.xpath('//*[@id="post-date"]/text()').extract()[0]
        item['time']=time

    def _extract_author(self,sel,item):
        pass
    def _extract_editor(self,sel,item):
        item['editor']='Nobody'
        pass 
