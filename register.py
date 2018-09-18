# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time,threading,random,string

reginfo = {
}

def getRandomString():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

def register(driver):
    headingText = driver.find_element_by_id("headingText")
    if headingText.text == "创建您的 Google 帐号":
        # 找到输入框并输入查询内容
        last_name = driver.find_element_by_id("lastName")
        reginfo['lastName'] = getRandomString()
        last_name.send_keys(reginfo['lastName'])
        firstName = driver.find_element_by_id("firstName")
        reginfo['firstName'] = getRandomString()
        firstName.send_keys(reginfo['firstName'])
        user_name = driver.find_element_by_id("username")
        reginfo['username'] = getRandomString()
        user_name.send_keys(reginfo['username'])
        passwd = driver.find_element_by_name("Passwd")
        reginfo['password'] = getRandomString()
        passwd.send_keys(reginfo['password'])
        confirm_passwd = driver.find_element_by_name("ConfirmPasswd")
        confirm_passwd.send_keys(reginfo['password'])
        accountDetailsNext = driver.find_element_by_id("accountDetailsNext")
        # 提交表单
        accountDetailsNext.click()
    elif headingText.text == "验证您的手机号码":
      try:
        code = driver.find_element_by_id("code")
        gradsIdvVerifyNext = driver.find_element_by_id("gradsIdvVerifyNext")
        gradsIdvVerifyNext.click()
      except Exception as e:
        phoneNumberId = driver.find_element_by_id("phoneNumberId")
        gradsIdvPhoneNext = driver.find_element_by_id("gradsIdvPhoneNext")
        gradsIdvPhoneNext.click()

    start_timer()

# 注册操作
def operationReg(driver):
    url = "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Fchrome%2Fsync%2Ffinish%3Fcontinue%3Dhttps%253A%252F%252Fwww.google.com%252F%26est%3DAASr9eppzKGHq0psjiQdMn8D-evgJvchiqn7UJYHhKeXEu-Z4NGWcn9ajFNpTk9w6fc7CobMpSE6ecH5y9y75w&flowName=GlifWebSignIn&flowEntry=SignUp"
    driver.get(url)
    start_timer()

def start_timer():
    timer = threading.Timer(5, register, (driver,))
    timer.start()


# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    operationReg(driver)
