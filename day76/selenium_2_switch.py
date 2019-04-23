"""
当页面中出现对话框 alert,或 内嵌窗口iframe
如果查找的元素节点在alert或iframe中的话，则需要切入到alert或iframe中
）driver.switch_to.frame()
）driver.switch_to.window(window_name)
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

driver = Chrome('driver/chromedriver')
url = 'https://qzone.qq.com/'

driver.get(url)

# 找查"帐号密码登录" 的<a>标签  id = switcher_plogin
# 查询元素如果不存在的话，则会报异常 NoSuchElementException

# 注意： 通过分析html, "帐号密码登录" 的<a>标签是在 <iframe id=login_frame>中
iframe = driver.find_element_by_id('login_frame')
driver.switch_to.frame(iframe)

a = driver.find_element_by_id('switcher_plogin')
print(a)
a.click()  # 点击

time.sleep(5)
driver.find_element_by_id('u').send_keys('610039018')
time.sleep(1)
driver.find_element_by_id('p').send_keys('aadkdkdjdjdkdkdd')
time.sleep(1)
driver.find_element_by_id('login_button').click()
time.sleep(2)

# 当登录成功之后，提取当前浏览器的cookies信息
# 将cookies转成字典，可以传给requests或urllib的Cookie处理器的CookieJar对象
cookies = driver.get_cookies() # [{'name': '', 'value': ''}, {}]
print(cookies)  # 当前站点下的所有cookie（domain, path, expire, name, value）
# 生成Cookie 样本 key=value&key=value
headers = {
    'Cookie': 'pgv_pvid=2354502640; pgv_pvi=9756064768; RK=xEwZe7uAO7; '
              'ptcz=719eb19959ad29defb12cc507883606074e95c3c9e7d6695baecf1dc8659bd03; '
              'ptui_loginuin=610039018; pgv_si=s7502236672; pgv_info=ssid=s4892807235;'
              ' _qz_referrer=qzone.qq.c'
}

cookie_list = [item['name']+'='+item['value'] for item in cookies]
cookie_str = ';'.join(cookie_list)
print(cookie_str)

driver.quit()