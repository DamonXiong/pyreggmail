# encoding=utf8

import pandas as pd


def dealData():
    df = pd.read_excel('./矮小数据.xls', 'Sheet1')
    dt_split = df["服用可乐定1小时后血压"].str.split('/')
    df["服用后舒张压"] = dt_split.str[1]
    df["服用后收缩压"] = dt_split.str[0]
    df.to_excel(
        './矮小数据_new.xls', 'Sheet1')


dealData()
