import lxml.html
def test():
    with file('tmp.txt') as f:
        etree=lxml.html.fromstring(f.read())
    node=etree.xpath('//div[@class="txt-box"]//a/@href')
    for i in node:
        print i


test()