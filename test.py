# encoding=utf8

import string
from urllib import parse, request
import json
import datetime
import os


def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()


# 方法主入口
if __name__ == '__main__':
    mobiles = ['13408418572']

    header_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    for i in mobiles:
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=00867051c88c08d5682fcdb6e94284f7e09834164e01&itemid=147&mobile=' + i
        RELEASE = request.urlopen(request.Request(
            url=url, headers=header_dict)).read().decode(encoding='utf-8')
        if RELEASE == 'success':
            print('号码成功释放')
        elif RELEASE == '2007':
            print('号码已被释放')

    # file_name = '.\\data\\' + datetime.datetime.now().strftime('%Y%m%d') + '.txt'
    # f = open(file_name, 'a', encoding='utf-8')  # 文件路径、操作模式、编码  # r''
    # f.write(json.dumps(reginfo) + '\n')
    # f.close()
    # fname = 'test163.txt'
    # with open(fname, 'r') as f:  # 打开文件
    #   lines = f.readlines()  # 读取所有行
    #   last_line = lines[-1]  # 取最后一行
    #   print(last_line)
    #   print(last_line.strip().strip('\n').split('----'))
    #   curr = lines[:-1]
    # file = open(fname, 'w')
    # file.writelines(curr)
    # file.close()
