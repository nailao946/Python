from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def 驱动():
    wz=r'C:\Users\Lenovo\AppData\Local\360Chrome\Chrome\Application\360chrome.exe'
    co = Options()
    co.binary_location = wz
    drive= r"D:\Tool\chromedriver.exe"
    d=webdriver.Chrome(executable_path=drive,options=co)  # 实例化一个浏览器
    return d
驱动()