#coding=utf-8 
import urllib,urllib2,re,json,bs4
from bs4 import BeautifulSoup

def wxspider():
	new_100=[]
	biz='__biz=MzA3MzM1NDYwMQ'
	for i in range(1,12):
		send_headers={ 'Connection':'keep-alive','Cookie':('ABTEST=3|1437121298|v1; IPLOC=CN1100; SUID=CC5A69A22708930A0000000055A8BB12; SUID=CC5A69A27728920A0000000055A8BB13; SUV=00161002A2695ACC55A8BB13AF1DE005; weixinIndexVisited=1; SNUID=FE685B9332342A3CD02984B4323FE856; sct=3; wapsogou_qq_nickname='
			' sct=2; wapsogou_qq_nickname='),
			'Host':'weixin.sogou.com','Referer':('http://weixin.sogou.com/gzh?openid=oIWsFt4GjSspUZWZoLgTrfqZUe1M'),
			'User-Agent':(
			'Mozilla/5.0 (Macintosh; '
			'Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) '
			'Chrome/43.0.2357.134 Safari/537.36')}
		data={}
		data = urllib.urlencode(data)  
		xfurl=('http://weixin.sogou.com/'
			'gzhjs?cb=sogou.weixin.gzhcb'
			'&openid=oIWsFt1mdY_3guZraCVTSTqnE5U0'
			'&eqs=OpsuoZygsqaHojL8ZMTfYuVxJ7lz5GBqWUuyg8mcK8Gt2enq0gKj4CMvXJvvGnoPdgSBC'
			'&ekv=7&page=%s&t=1437121380890'%i)
		url=r'http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFt4GjSspUZWZoLgTrfqZUe1M&eqs=O%%2Bs9oM7gJi0ioec5WulAlu%%2F5VqPlL06X60cCoE2vZ%%2F6eDCc7g5L5oyQ8OIHH4YMHBApVQ&ekv=7&page=%s&t=1437152238526'%i
		request = urllib2.Request(url,headers=send_headers)
		response=urllib2.urlopen(request)	
		html=response.read()
		print html
		m=re.search(r'sogou.weixin.gzhcb\((?P<json>.*)\)',html)
		html_json=m.groupdict('json')['json']
		json1=json.loads(html_json)
		for every_item in json1['items']:
			_item=every_item.encode('gbk')
			soup = BeautifulSoup(every_item, 'html.parser')
			new_100.append(soup.title.string+':'+soup.url.string)
	print new_100
	f=file('dll.txt','w')
	for every in new_100:
		f.write(every+'\n')
def writethetext():
	html='''
	sogou.weixin.gzhcb({"totalItems":3,"totalPages":1,"page":1,"items":["<?xml version="1.0" encoding="gbk"?><DOCUMENT><docid><\/docid><item> <key><![CDATA[http://mp.weixin.qq.com/]]><\/key><tplid><![CDATA[555]]><\/tplid><classid>11002601<\/classid> <display> <docid>ab735a258a90e8e1-6bee54fcbd896b2a-b4e45757f4eb9036f84ed7ffff4b6125<\/docid> <tplid>550<\/tplid><title><![CDATA[只是不想复习来推首歌><]]><\/title><url><![CDATA[http://mp.weixin.qq.com/s?__biz=MzAwNDQ3MDIwMA==&mid=209553523&idx=1&sn=28c82c58a516928c8e78efe3e87014ec&3rd=MzA3MDU4NTYzMw==&scene=6#rd]]><\/url><title1><![CDATA[只是不想复习来推首歌><]]><\/title1><imglink><![CDATA[http://mmbiz.qpic.cn/mmbiz/pMnSO0kyANpGETWGoRIuokL02BD7LEicViaqPjKIpee7f6LKCtibwk71icLbhaWWYoznWV5rHXbAiaVrqfmYXO3noyg/0?wx_fmt=jpeg]]><\/imglink><headimage><![CDATA[http://wx.qlogo.cn/mmhead/Q3auHgzwzM6umK99HlKMz4d8zGM998fErzCFgd3HEL8NeIuAZWm7ag/0]]><\/headimage><sourcename><![CDATA[没有被通过的名字是有多可怜]]><\/sourcename><content168><![CDATA[不废话,只是来推几首兼有节奏感的小清新(别吐槽我啦= =)祝大家期末复习背书不困啦~\\(≧▽≦)/~啦啦啦]]><\/content168><site><![CDATA[http://music.163.com/outchain/player?type=2&id=24615856&auto=1&height=66]]><\/site><isV><![CDATA[0]]><\/isV><openid><![CDATA[oIWsFt4GjSspUZWZoLgTrfqZUe1M]]><\/openid><content><![CDATA[不废话,只是来推几首兼有节奏感的小清新(别吐槽我啦= =)祝大家期末复习背书不困啦~\\(≧▽≦)/~啦啦啦]]><\/content><showurl><![CDATA[微信 - mp.weixin.qq.com]]><\/showurl><date><![CDATA[2015-6-14]]><\/date><pagesize><![CDATA[11k]]><\/pagesize> <lastModified>1434294098<\/lastModified><pagesize>12k<\/pagesize> <\/display><\/item><\/DOCUMENT>","<?xml version="1.0" encoding="gbk"?><DOCUMENT><docid><\/docid><item> <key><![CDATA[http://mp.weixin.qq.com/]]><\/key><tplid><![CDATA[555]]><\/tplid><classid>11002601<\/classid> <display> <docid>ab735a258a90e8e1-6bee54fcbd896b2a-aa858bd623cd06fcc07658d59c140454<\/docid> <tplid>550<\/tplid><title><![CDATA[好久不见哎哎哎~~]]><\/title><url><![CDATA[http://mp.weixin.qq.com/s?__biz=MzAwNDQ3MDIwMA==&mid=209347586&idx=1&sn=9681ade5c33de6415cf90ca2136ce83c&3rd=MzA3MDU4NTYzMw==&scene=6#rd]]><\/url><title1><![CDATA[好久不见哎哎哎~~]]><\/title1><imglink><![CDATA[http://mmbiz.qpic.cn/mmbiz/pMnSO0kyANqCgUIYUSeK2fZjibhiaibgw2r1utQWxhbb7zKsy0T3XcvFHRgJw3AMcVA75u0s8mziaqGwD5q3cv2Lyw/0?wx_fmt=jpeg]]><\/imglink><headimage><![CDATA[http://wx.qlogo.cn/mmhead/Q3auHgzwzM6umK99HlKMz4d8zGM998fErzCFgd3HEL8NeIuAZWm7ag/0]]><\/headimage><sourcename><![CDATA[没有被通过的名字是有多可怜]]><\/sourcename><content168><![CDATA[听说微信平台上线了新功能,可以播放音乐了,好奇主页君来试试期末季来得太快就像龙卷风o(╯□╰)o有没有快被吹跑了哎哎哎明天主页君有4个ddl还有一个脱稿pre=_=,祝我顺利度过黑暗星期四吧~~放一首Immortals [From ＂Big Hero＂] 来醒醒脑,刷夜是还是需要这样燃的音乐啊T^T.大家...]]><\/content168><isV><![CDATA[0]]><\/isV><openid><![CDATA[oIWsFt4GjSspUZWZoLgTrfqZUe1M]]><\/openid><content><![CDATA[听说微信平台上线了新功能,可以播放音乐了,好奇主页君来试试期末季来得太快就像龙卷风o(╯□╰)o有没有快被吹跑了哎哎哎明天主...]]><\/content><showurl><![CDATA[微信 - mp.weixin.qq.com]]><\/showurl><date><![CDATA[2015-6-10]]><\/date><pagesize><![CDATA[8k]]><\/pagesize> <lastModified>1433945503<\/lastModified><pagesize>9k<\/pagesize> <\/display><\/item><\/DOCUMENT>","<?xml version="1.0" encoding="gbk"?><DOCUMENT><docid><\/docid><item> <key><![CDATA[http://mp.weixin.qq.com/]]><\/key><tplid><![CDATA[555]]><\/tplid><classid>11002601<\/classid> <display> <docid>ab735a258a90e8e1-6bee54fcbd896b2a-3e6ed7a78a8eda756813a5a5b0618aad<\/docid> <tplid>550<\/tplid><title><![CDATA[被某个女同学逼着发李光洙的推送T_T不发就要给100块ヽ(...]]><\/title><url><![CDATA[http://mp.weixin.qq.com/s?__biz=MzAwNDQ3MDIwMA==&mid=207505515&idx=1&sn=676f4746aa82a880bf180385b07bc20a&3rd=MzA3MDU4NTYzMw==&scene=6#rd]]><\/url><title1><![CDATA[被某个女同学逼着发李光洙的推送T_T不发就要给100块ヽ(≧Д≦)ノ我是无辜的╭(╯^╰)╮]]><\/title1><imglink><![CDATA[http://mmbiz.qpic.cn/mmbiz/pMnSO0kyANq0XKyhgeUWobP8ns1D2SYRQ46ylhQu8sd23rmBO1bmCk11ibIHlGlCSJH2COCuc1sZLkMbyo4RYXQ/0?wx_fmt=jpeg]]><\/imglink><headimage><![CDATA[http://wx.qlogo.cn/mmhead/Q3auHgzwzM6umK99HlKMz4d8zGM998fEiaJMXEEQomNy1WSafO11L9w/0]]><\/headimage><sourcename><![CDATA[没有被通过的名字是有多可怜]]><\/sourcename><content168><![CDATA[今天推送李光洙!你们认识他是谁吗!说实话,主页君并不了解这货是谁⊙_⊙毕竟我这么爱国,都没有看过running man~(其实,我连奔跑吧兄弟都没有看完过几集(;一_一))不过一直有一个花痴女同学在我旁边balabala安利这货,从上课到下课到讨论!简直骨灰粉花痴粉!简直不能忍!...]]><\/content168><isV><![CDATA[0]]><\/isV><openid><![CDATA[oIWsFt4GjSspUZWZoLgTrfqZUe1M]]><\/openid><content><![CDATA[今天推送李光洙!你们认识他是谁吗!说实话,主页君并不了解这货是谁⊙_⊙毕竟我这么爱国,都没有看过running man~(其实,我...]]><\/content><showurl><![CDATA[微信 - mp.weixin.qq.com]]><\/showurl><date><![CDATA[2015-4-29]]><\/date><pagesize><![CDATA[38k]]><\/pagesize> <lastModified>1430294691<\/lastModified><pagesize>39k<\/pagesize> <\/display><\/item><\/DOCUMENT>"]})
		'''
	re.sub(r'\t\n\r','',html)
	m=re.search(r'sogou.weixin.gzhcb\((?P<json>.*)\)',html)
	html_json=m.groupdict('json')['json']
	json1=json.loads(html_json)
	print html_json
	#for every_item in json1['items']:
	#	_item=every_item.decode('utf-8')
	#	print _item
	#	soup = BeautifulSoup(every_item, 'html.parser')
	#	new_100.append(soup.title.string+':'+soup.url.string)
	#print new_100
	#f=file('dll.txt','w')
	#for every in new_100:
	#	f.write(every+'\n')


def pretext():
	f=file('a.txt','r')
	text=f.read()
	text=text.replace('http://',r'\rhttp://')
	f2=file('b.txt','w')
	f2.write(text)
	print text
writethetext()
