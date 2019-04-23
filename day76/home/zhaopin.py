import requests
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common import by
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions

"""
搜索Python岗位的数据接口：
"""
url = 'https://fe-api.zhaopin.com/c/i/sou'
params = {
    "pageSize": 90,
    "cityId": 854,
    "workExperience": -1,
    "education": -1,
    "companyType": -1,
    "employmentType": -1,
    "jobWelfareTag": -1,
    "kw": "python",
    "kt": 3,
    "_v": 0.58082932,
    "x-zp-page-request-id": "5eb53de10d6e45539ce97a3045d4b60d-1555981987134-645817"
}

"""
查询城市的code
"""
url = 'https://fe-api.zhaopin.com/c/i/city-page/user-city'
params = {
    'ipCity': '西安',
    'ipProvince': '陕西',
    'userDesiredCity': '',
    '_v': '0.11237429',
    'x-zp-page-request-id': '70a78cca30fb4909ae136ff08c59237e-1555982448012-671231'
}


"""
西安城市的智联Python岗位数据
"""
url ='https://sou.zhaopin.com/?jl=854&kw=python&kt=3'

# resp = requests.get(url)  # requests请求下载

driver = Chrome('../driver/chromedriver')

def download():

    driver.get(url)  # 如果网页是ajax执行时， 此时不会阻塞
    # 设置阻塞的条件，如， 直到某一ajax执行完之后的element出现为止
    ui.WebDriverWait(driver, 60).until(expected_conditions.visibility_of_all_elements_located((by.By.CLASS_NAME, 'soupager')))

    time.sleep(2)

    # 关闭弹出的模态对话框：
    ok_btn = driver.find_element_by_class_name('risk-warning__content').find_element_by_tag_name('button')
    ok_btn.click()

    page = 1
    while page < 10:
        # 滚动屏幕到底部
        to_position = 1500
        for i in range(10):
            driver.execute_script('var q = document.documentElement.scrollTop=%s' % ((i+1)*to_position) )
            time.sleep(0.5)

        ui.WebDriverWait(driver, 60).until(
            expected_conditions.visibility_of_all_elements_located((by.By.CLASS_NAME, 'soupager')))

        parse(driver.page_source)
        # 获取下一页的数据
        # bug
        # next_btns = driver.find_elements_by_xpath('//div[@class="soupager"]/button')
        next_btns = driver.find_element_by_class_name('soupager').find_elements_by_tag_name('button')
        next_page = next_btns[1] # 第二个按钮
        print(next_page.rect, next_page.location)
        # next_page.click()

        driver.execute_script('var q = document.documentElement.scrollTop=%s' % (int(next_page.location['y'])-200))
        time.sleep(5)
        next_page.click()

        time.sleep(2)


        page += 1

    driver.quit()


def parse(html):  # 提取数据
    pass

if __name__ == '__main__':
    download()

