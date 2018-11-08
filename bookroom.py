# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.select import Select
import time
import threading
import random
import string
from urllib import parse, request
import re
import json
import datetime
from datetime import timedelta, date

isChrome = True
startHour = 23
startMin = 58
userName = '2160652004'
passWord = '270749'
roomName = '研究间17'
startTime = '800'
endTime = '2200'
bookDate = date.today()+timedelta(2)
isSlectDate = False


# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=option)
    # 打开chrome浏览器
    # driver = webdriver.Chrome()
    return driver


# 前台开启浏览器模式
def openEdge():
    driver = webdriver.Edge()
    return driver

def goLogin(driver):
    try:
      username = driver.find_element_by_id("username")
      password = driver.find_element_by_id("password")
      username.send_keys(userName)
      password.send_keys(passWord)
      driver.find_element_by_class_name('btn-success').click()
      return True
    except Exception as e:
      print(str(e))
      return False

def goUserCenter(driver):
  try:
    confirmDlg = driver.find_element_by_id("uni_confirm")
    if not confirmDlg.get_attribute("display") == "block":
      return False
    driver.find_element_by_class_name(
        'ui-dialog-titlebar-close').click()
    driver.find_element_by_id('user_center').click()
    return True
  except Exception as e:
    print(str(e))
    return False

def goBookRoomSelection(driver):
  try:
    title = driver.find_element_by_class_name('h_title')
    if title.text == 'Home Page':
      driver.find_element_by_link_text('研究小间').click()
      return True
    else:
      return False
  except Exception as e:
    print(str(e))
    return False

def changeTheDate(driver):
  global roomName,isSlectDate
  try:
    datetitles = driver.find_elements_by_class_name('cld-h-cell')
    isFindDateTitle = False
    print(bookDate)
    for i in range(len(datetitles)):
      if datetitles[i].get_attribute('date') == str(bookDate):
        isFindDateTitle = True
        if datetitles[i].get_attribute('class').find('cld-d-sel') == -1:
          datetitles[i].click()
        else:
          if isSlectDate:
            isSlectDate=False
            if i == 6:
              datetitles[5].click()
            else:
              datetitles[i+1].click()
          else:
            isSlectDate=True
    
    if not isFindDateTitle:
      datetitles[9].click()
    else:
      roomtitles = driver.find_elements_by_class_name('cld-obj-qz')
      for i in range(len(roomtitles)):
        if roomtitles[i].get_attribute('objname') == roomName:
          if len(roomtitles[i].find_elements_by_class_name('cld-ttd')) > 2:
            roomtitles[i].find_element_by_class_name('cld-ttd-title').click()
            break

    return True
  except Exception as e:
    print(str(e))
    return False

def comitBook(driver):
  try:
    dialogtitle = driver.find_element_by_class_name('ui-dialog-title')
    if dialogtitle.text == '预约申请':
      st = driver.find_elements_by_name('start_time')[2]
      et = driver.find_elements_by_name('end_time')[2]
      Select(st).select_by_value(startTime)
      Select(et).select_by_value(endTime)
      driver.find_element_by_class_name('submitarea').find_element_by_xpath(
          "//input[@value='提交']").click()
      return True
    else:
      return False
  except Exception as e:
    print(str(e))
    return False

def book_room(driver):
    global isChrome, userName, passWord

    if driver.title == "IC空间管理系统":
      if not goLogin(driver):
        print('not login')
        if goUserCenter(driver):
          return
        else:
          print('not go user center')
          if not goBookRoomSelection(driver):
            print('not go 研究小间')
            if not comitBook(driver):
              print('not go commit')
              if not changeTheDate(driver):
                print('not go Date')


    start_timer(driver)

# 注册操作
def operationBook(driver):
    global startHour, startMin
    url = "http://seatlib.fjtcm.edu.cn"
    driver.get(url)
    start_timer(driver)


def start_timer(driver, time=0.5):
    timer = threading.Timer(time, book_room, (driver,))
    timer.start()


def openbrowser():
    global isChrome
    driver = {}
    if isChrome:
        driver = openChrome()
        isChrome = False
    else:
        driver = openEdge()
        isChrome = True

    operationBook(driver)


# 方法主入口
if __name__ == '__main__':
  
    while True:
        now = datetime.datetime.now()
        if now.hour > startHour or (now.hour == startHour and now.minute >= startMin):
            break
        # 每隔60秒检测一次
        time.sleep(10)
    openbrowser()
