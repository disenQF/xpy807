"""
通过BS4,进行网页数据的解析
支持标签名、样式和属性的网页数据提取。
相对于xpath的查询路径语法，bs4提供了标准函数的
"""
import os
import requests
from bs4 import BeautifulSoup

from util import header
from es_api import doc, index

def download(url, params=None, data=None, json=None):
    print('downloading ', url)

    if os.path.exists('boss_python.html'):
        parse(open('boss_python.html', 'r', encoding='utf-8'))
        return
    resp = requests.get(url, params=params, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.103 Safari/537.36'
    })
    # resp.status_code
    # resp.url
    # resp.text
    # resp.encoding
    # resp.headers
    # resp.cookies
    # resp.json()
    with open('boss_python.html', 'w+', encoding='utf-8') as file:
        file.write(resp.text)

        # 写完之后，文本光标是在文件的尾部，
        # 如果再一次读取时，必须将光标移动到文件开始的位置
        file.seek(0)

        parse(file)


def parse(html):
    # if isinstance(html, str):
    #     print(html)
    # else:
    #     print(html.read())
    soup = BeautifulSoup(html, 'lxml')  # 根节点
    title_node = soup.find('title')  # 只查找一个标签节点
    print(title_node.text, title_node.name)

    ul_node = soup.find('ul')  # BS4的节点对象

    primary_list = soup.find_all('div', class_="job-primary")
    print("primary count", len(primary_list))

    for primary in primary_list:
        job_title = primary.find('div', class_="job-title").text
        salary = primary.find('span', class_='red').text

        p_info = primary.find('p').contents
        job_city, job_years, edu_level = tuple([item.strip() for item in p_info if isinstance(item, str)])

        # 查询公司名称
        company_name = primary.find('div', class_="company-text").find('a').text

        print(job_title, salary, job_city, job_years, edu_level, company_name)
        itempipeline({
            'title': job_title,
            'salary': salary,
            'city': job_city,
            'years': job_years,
            'education': edu_level,

        })


def itempipeline(item):
    global job_num
    doc.add_doc(index_name='boss', type_name='job', doc_id=job_num, **item)
    job_num += 1


if __name__ == '__main__':

    # 先删除索引
    requests.delete('http://localhost:9200/boss')

    # 再添加索引
    index.add_index('boss')
    job_num = 1

    url = 'https://www.zhipin.com/job_detail/'
    params = {
        "query": "python",
        "city": "101110100",
        "page": "1",
        "ka": "page-next"
    }

    download(url, params=params)
