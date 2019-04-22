import time
from selenium.webdriver import Chrome

# 创建Chrome驱动对象- 打开chrome浏览器
driver = Chrome('driver/chromedriver')

# 访问url
driver.get('http://www.baidu.com')  # 阻塞到页面加载完成

# 在百度搜索中，搜索"西安千锋"
# 1) 查找输入框，向输入框加设置内容
# 2） 查找搜索按钮，点击按钮

# 根据标签的id查找输入框
input_element = driver.find_element_by_id('kw')
if input_element:
    # 将内容发送到页面输入框中
    input_element.send_keys('西安千锋')


time.sleep(2)

search_btn = driver.find_element_by_id('su')
if search_btn:
    search_btn.click()  # 点击搜索按钮

time.sleep(2)
driver.save_screenshot('baidu.png')  # 载屏

driver.quit()  # 关闭浏览器