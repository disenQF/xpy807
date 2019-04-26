import requests
from lxml import etree
from util.header import get_headers


resp = requests.get('https://www.qidian.com/free/all', headers=get_headers())

root = etree.HTML(resp.text)

links = root.xpath('//div[@class="work-filter type-filter"]//a/@href')
print(links)