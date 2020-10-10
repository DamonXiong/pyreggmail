# encoding=utf8

import pandas as pd


def inputHeight():
    dfheight = pd.read_excel('./20191223/身高.xls', 'SQL Results')
    df = pd.read_excel(
        './20191223/2019.12.24--分析汇总表(inputheight).xlsx', 'Sheet1')
    for i, row in df.iterrows():
        if row['身高'] == 0:
            serie = dfheight.loc[dfheight['身份号'] == row['身份证号码']]['身高'];
            if len(serie.values) > 0:
                # print(serie)
                df.loc[i, '身高'] = serie.values[0]
    df.to_excel('./20191223/2019.12.24--分析汇总表(inputheight)_done.xlsx', 'Sheet1')
    print("getHeight steps complete")


inputHeight()
