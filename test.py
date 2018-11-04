# encoding=utf8

import string
from urllib import parse, request
import json
import datetime


def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()


# 方法主入口
if __name__ == '__main__':
    mobiles = ['17160652713']

    header_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    for i in mobiles:
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=00867051741e601d25b99c10cca6e5cf6456983a&itemid=147&mobile=' + i
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
