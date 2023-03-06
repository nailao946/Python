from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
driver = webdriver.Edge(executable_path=r'D:\Tool\edgedriver_win64\msedgedriver.exe')
driver.get(url=r'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果标签在frame里面需要 切换标签定位到frame
# 里面填写frame的id标签
driver.switch_to.frame('iframeResult')

biaoqian = driver.find_element_by_id('draggable')

# 创建个动作链
action = ActionChains(driver)
# 长按
action.click_and_hold(biaoqian)
for i in range(5):
    # 使用move_by_offset时候有两个参数，（x,y），移动的x值和移动的y值
    # 单位是像素
    action.move_by_offset(17,0).perform()
    sleep(0.5)
action.release(biaoqian)
driver.quit()

