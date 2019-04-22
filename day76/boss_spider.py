import os
import re
import csv
from threading import Thread

import time
from bs4 import BeautifulSoup
import requests


class BossSpider(Thread):
    start_url = 'https://www.zhipin.com/job_detail/'
    params = {
        "query": "python",
        "city": "101110100",
        "page": "1",
        "ka": "page-next"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.103 Safari/537.36'
    }

    download_per_delay = 3  # 每隔3秒发起一次下载请求

    csv_filename = 'boss.csv'  # 数据存储的位置

    def run(self):
        self.download()  # 开始下载

    def download(self):
        resp = requests.get(self.start_url, self.params, headers=self.headers)

        if resp.status_code == 200:
            print(resp.url, '下载成功!')

            html = resp.text
            self.parse(html)  # 解析数据

    def parse(self, html):
        root = BeautifulSoup(html, 'lxml')

        # 查找所有 class=job-primary的div
        job_nodes = root.select('.job-primary')

        items = []  # 批量写入

        for job_tag in job_nodes:
            info_a_tag = job_tag.select_one('div[class="info-primary"] a')
            info_href = info_a_tag.attrs.get('href')  # 获取详情的url地址
            job_name = info_a_tag.select_one('.job-title').text
            job_salary_range = info_a_tag.select_one('.red').text

            # 提取公司的名称、城市位置、年限、学历
            p_tag = job_tag.select_one('div[class="info-primary"] p')

            # 只提取p标签中的所有文本
            p_texts = [item for item in p_tag.contents if isinstance(item, str)]
            address, years, education = tuple(p_texts)

            company_a = job_tag.select_one('.info-company a')
            company_url = company_a.attrs.get('href')
            company_name = company_a.text

            items.append({
                'job_url': info_href,
                'job_name': job_name,
                'salary_range': job_salary_range,
                'address': address,
                'years': years,
                'education': education,
                'company_url': company_url,
                'company_name': company_name
            })

        print('本页提取数据完成，共%s 条数据！' % len(items))

        self.csv_pipeline(items)

        # 提取下一页
        next_a = root.select_one('.page .next')
        if 'disabled' in next_a.attrs.get('class'):
            print('--%s 城市中的所有 %s 岗位爬取完成--' % (self.params.get('city'), self.params.get('query')))
        else:
            next_href = next_a.attrs.get('href')
            page = re.findall(r'page=(\w+)', next_href)[0]
            ka = next_a.attrs.get('ka', 'page-next')

            self.params['page'] = page
            self.params['ka'] = ka

            time.sleep(self.download_per_delay)
            self.download() # 开始下载下一页

    def csv_pipeline(self, items: list):
        existed_header = os.path.exists(self.csv_filename)
        with open(self.csv_filename, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=items[0].keys())
            if not existed_header:
                writer.writeheader()  # 写入标题

            for item in items:
                writer.writerow(item)


if __name__ == '__main__':
    print('-start spider--')
    spider = BossSpider()
    spider.start()

    spider.join()

    print('--exit spider-')