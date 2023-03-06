from selenium import webdriver
# https://blog.csdn.net/weixin_36279318/article/details/79475388
from time import sleep
# 导入动作链
from selenium.webdriver import ActionChains
web = webdriver.Edge(executable_path=r'D:\Tool\edgedriver_win64\msedgedriver.exe')  # 实例化一个浏览器对象（传入浏览器的驱动）
web.get(url='https://www.taobao.com/')  # 让浏览器发出一个请求
# page_text = web.page_source  # 获取源代码

# 标签定位
search_input = web.find_element_by_id('q')
# 标签交互
search_input.send_keys('小米')
# 搜索class（css标签）标签
btn = web.find_element_by_css_selector('.btn-search')
btn.click()  # 点击按钮

web.get('https://www.baidu.com/')  # 请求网址到baidu
web.back()  # 返回上一级

# web.forward()  # 向前一级
# web.execute_script() # 执行js
sleep(5)
web.quit()  # 退出网页
# web.find_elements_by_css_selector()