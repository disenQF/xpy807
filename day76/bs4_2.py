"""
使用bs4的select来解析数据 【重点】
1） 标签选择
    soup.select('div') 返回所有的div标签对象
2） class样式选择
    soup.select(".list-primary") 返回所有class="list-primary"的标答对象

3） id选择
    soup.select('#info')

4)  属性选择
    soup.select('div[class=list-primary]')

5) 层级标签选择
    soup.select('div > a')  div的直接子标签
    soup.select('div[class=info-primary] > h3')
    soup.select('div p')  div下的所有p标签
"""
import re

from bs4 import BeautifulSoup, Tag

def parse(html: str):
    root = BeautifulSoup(html, 'lxml')  # bs4依赖lxml库

    primary_list = root.select('.job-primary') # list[bs4.element.Tag, ...]
    # print(type(primary_list[0]))
    for primary in primary_list:
        div_node: Tag = primary
        # Tag对象的属性 【重点】
        # div_node.text       标签文本信息
        # div_node.name       标签名
        # div_node.contents   所有子标签
        # div_node.next_siblings   下一个兄弟标签
        # div_node.attrs  标签属性集的对象

        # Tag对象的方法 【重点】
        # div_node.find()
        # div_node.find_all()
        # div_node.select()
        # div_node.select_one() 只选择第一个标签

        info_a = div_node.select_one('div[class="info-primary"] a')
        # print(info_a.attrs.get('href'))
        # print(info_a.contents)
        info_url = info_a.attrs.get('href')
        title = info_a.select_one('.job-title').text
        salary = info_a.select_one('.red').text

        p_node = div_node.select_one('div[class="info-primary"] p')
        address,  years, education = tuple([item for item in p_node.contents if isinstance(item, str)])
        print(info_url, title, salary, address, years, education)

    # 提取下一页(有可能没有下一页，则停止爬虫)
    next_node = root.select_one('.page .next')
    # 判断是否还有下一页
    if 'disabled' in next_node.attrs.get('class'):
        print('--当前城市的Python岗位 全部爬取完成---')
    else:
        next_href = next_node.attrs.get('href')
        ka = next_node.attrs.get('ka')  # page-next
        page = re.findall(r'page=(\d+)', next_href)[0]

        print(page, ka)


if __name__ == '__main__':
    html = None
    with open('boss_python.html', 'r') as f:
        html = f.read()

    parse(html)