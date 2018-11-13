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
import threading
from datetime import timedelta, date


class BookRoomThread(threading.Thread):

  startHour = 12
  startMin = 58
  userName = '2160652004'
  passWord = '270749'
  roomName = '研究间17'
  startTime = '800'
  endTime = '900'
  bookDate = date.today()+timedelta(1)
  isSlectDate = False

  def __init__(self, name):
      super().__init__()
      self.__running = threading.Event()      # 用于停止线程的标识
      self.__running.set()      # 将running设置为True
      self.name = name
      self.isStart = False

  def stop(self):
      if self.timer:
        self.timer.stop()
      if self.driver:
        self.driver.close()
      self.__running.clear()        # 设置为False

  def run(self):  # 固定名字run ！！！必须用固定名
      while self.__running.isSet():
        if not self.isStart:
          self.openbrowser()
          self.isStart = True
        time.sleep(1)

  # 前台开启浏览器模式
  def openChrome(self):
      # 加启动配置
      option = webdriver.ChromeOptions()
      option.add_argument('disable-infobars')
      self.driver = webdriver.Chrome(chrome_options=option)
      # 打开chrome浏览器
      # driver = webdriver.Chrome()

  def goLogin(self):
      try:
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        username.send_keys(self.userName)
        password.send_keys(self.passWord)
        self.driver.find_element_by_class_name('btn-success').click()
        return True
      except Exception as e:
        print(str(e))
        return False

  def goUserCenter(self):
    try:
      dialogtitle = self.driver.find_element_by_id('ui-id-3')
      if dialogtitle.text == '提醒':
        self.driver.find_element_by_class_name('ui-button-text-only').click()
        return True
      else:
        return False
    except Exception as e:
      print(str(e))
      return False

  def goBookRoomSelection(self):
    try:
      title = self.driver.find_element_by_class_name('h_title')
      if title.text == 'Home Page':
        self.driver.find_element_by_link_text('研究小间').click()
        return True
      else:
        return False
    except Exception as e:
      print(str(e))
      return False

  def inUserCenter(self):
    try:
      title = self.driver.find_element_by_class_name('h_title')
      if title.text.strip() == '个人中心':
        result = self.driver.find_element_by_css_selector('.orange.uni_trans')
        if result.text.strip() == '预约成功':
          return True
        else: 
          self.driver.find_element_by_link_text('研究小间').click()
          return False
      else:
        return False
    except Exception as e:
      print(str(e))
      return False

  def changeTheDate(self):
    try:
      datetitles = self.driver.find_elements_by_class_name('cld-h-cell')
      isFindDateTitle = False
      print(self.bookDate)
      for i in range(len(datetitles)):
        if datetitles[i].get_attribute('date') == str(self.bookDate):
          isFindDateTitle = True
          if datetitles[i].get_attribute('class').find('cld-d-sel') == -1:
            datetitles[i].click()
          else:
            if self.isSlectDate:
              self.isSlectDate = False
              if i == 6:
                datetitles[5].click()
              else:
                datetitles[i+1].click()
            else:
              self.isSlectDate = True
      
      if not isFindDateTitle:
        datetitles[9].click()
      else:
        roomtitles = self.driver.find_elements_by_class_name('cld-obj-qz')
        for i in range(len(roomtitles)):
          if roomtitles[i].get_attribute('objname') == self.roomName:
            if len(roomtitles[i].find_elements_by_class_name('cld-ttd')) > 2:
              roomtitles[i].find_element_by_class_name('cld-ttd-title').click()
              break

      return True
    except Exception as e:
      print(str(e))
      return False

  def comitBook(self):
    try:
      dialogtitle = self.driver.find_element_by_class_name('ui-dialog-title')
      if dialogtitle.text == '预约申请':
        st = self.driver.find_elements_by_name('start_time')[2]
        et = self.driver.find_elements_by_name('end_time')[2]
        Select(st).select_by_value(self.startTime)
        Select(et).select_by_value(self.endTime)
        self.driver.find_element_by_class_name('submitarea').find_element_by_xpath(
            "//input[@value='提交']").click()
        return True
      else:
        return False
    except Exception as e:
      print(str(e))
      return False

  def book_room(self):
      if self.driver.title == "IC空间管理系统":
        if not self.goLogin():
          print('not login')
          if not self.inUserCenter():
            print('not in user center')
            if not self.goUserCenter():
              print('not go user center')
              if not self.comitBook():
                print('not go 研究小间')
                if not self.changeTheDate():
                  print('not go commit')
                  if not self.goBookRoomSelection():
                    print('not go Date')
          else:
            print('book success')
            self.driver.close()
            self.stop()
            return


      self.start_timer()

  # 注册操作
  def operationBook(self):
      url = "http://seatlib.fjtcm.edu.cn"
      self.driver.get(url)

      while True:
          now = datetime.datetime.now()
          if now.hour > self.startHour or (now.hour == self.startHour and now.minute >= self.startMin):
              self.driver.refresh()
              break
          # 每隔10秒检测一次
          time.sleep(10)
      self.start_timer()

  def start_timer(self, interval=0.5):
      self.timer = threading.Timer(interval, self.book_room)
      self.timer.start()

  def openbrowser(self):
      self.openChrome()
      self.operationBook()
