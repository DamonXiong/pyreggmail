# encoding=utf8

import pandas as pd


def repeatData():
    dftemp = pd.read_excel('./20191224/2019.12.24--分析汇总表(inputhighpress).xlsx', 'Sheet1')
    newdata = {}
    print('read excel done')
    for i, row in dftemp.iterrows():
        if row['高血压'] == '是':
            if row['身份证号码'] not in newdata.keys():
                newdata[row['身份证号码']] = {0: row['出生日期'], 1: row['高血压']}
    print("repeatData step 1 complete")
    for i, row1 in dftemp.iterrows():
        if row1['身份证号码'] in newdata.keys():
            if row1['出生日期'] == newdata[row1['身份证号码']][0]:
                dftemp.loc[i, '高血压-填充'] = '是'
            else:
                dftemp.loc[i, '高血压-填充'] = '否'
        else:
            dftemp.loc[i, '高血压-填充'] = '否'
    print('step2 complete')
    dftemp.to_excel(
        './20191224/2019.12.24--分析汇总表(inputhighpress)-repeat.xlsx', 'Sheet1')
    print("repeatData steps complete")


repeatData()
