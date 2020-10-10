# encoding=utf8

import pandas as pd


def read_info():
    df = pd.read_excel("发卡行简称.xlsx")
    print(df.pivot_table(index=['发卡行', '简称']))
    # print(df.describe())
    # print(df.发卡行.size)
    # print(df.发卡行.var())
    # print(df.mode())
    # result_dic = df.groupby('发卡行')['简称'].apply(list).to_dict()
    # print(result_dic)


read_info()
