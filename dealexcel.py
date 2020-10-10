# encoding=utf8

import numpy as np
import pandas as pd


def getHeight():
    dfheight = pd.read_excel('./excel/test.xls', 'SQL Results', usecols='B,H')
    newdata = {}
    for row in dfheight.itertuples():
        # print(row)
        if not np.isnan(row[2]):
            if row[1] not in newdata.keys():
                newdata[row[1]] = row[2]
    print("getHeight step 1 complete")
    rowindex = 0
    for row1 in dfheight.itertuples():
        if np.isnan(row1[2]) and row1[1] in newdata.keys():
            dfheight.loc[rowindex, '身高'] = newdata[row1[1]]
        rowindex += 1
    dfheight.to_excel('./excel/result.xls', 'SQL Results')
    print("getHeight steps complete")


def inputWeight():
    dfheight = pd.read_excel('./excel/2018年.xls', 'SQL Results', usecols='B,K')
    newdata = {}
    for row in dfheight.itertuples():
        if not np.isnan(row[2]):
            if row[1] not in newdata.keys():
                newdata[row[1]] = row[2]
    print("inputWeight step 1 complete")
    rowindex = 0
    for row1 in dfheight.itertuples():
        if np.isnan(row1[2]) and row1[1] in newdata.keys():
            dfheight.loc[rowindex, '孕前体重'] = newdata[row1[1]]
        rowindex += 1
    dfheight.to_excel('./excel/2018年_weight.xls', 'SQL Results')
    print("inputWeight steps complete")


def getBMI():
    df = pd.read_excel('./excel/test.xls', 'SQL Results', usecols='B,L')
    newdata = {}
    for row in df.itertuples():
        # print(row)
        if not np.isnan(row[2]):
            if row[1] not in newdata.keys():
                newdata[row[1]] = row[2]
    print("getBMI step 1 complete")
    rowindex = 0
    for row1 in df.itertuples():
        if np.isnan(row1[2]) and row1[1] in newdata.keys():
            df.loc[rowindex, '孕前体重指数'] = newdata[row1[1]]
        rowindex += 1
    df.to_excel('./excel/result.xls', 'SQL Results')
    print("getBMI steps complete")


def removeTheSameData():
    name = '2018年_sort'
    df = pd.read_excel('./excel/' + name + '.xls', 'SQL Results')

    df.drop_duplicates(['身份证号码', '孕周'], keep='last', inplace=True)
    df.to_excel(
        './excel/' + name + '_drop.xls', 'SQL Results')


def sortByWeek():
    name = '2018年'
    df = pd.read_excel('./excel/' + name + '.xls', 'SQL Results')
    dt_split = df["孕周"].str.split('+')
    df["孕周/周"] = dt_split.str[0]
    df["孕周/天"] = dt_split.str[1]
    # df["孕周2"] = np.where(len([0])
    #                      < 2, '0' + df["孕周"].str, df["孕周"])
    dt_split = df["血压"].str.split('/')
    df["舒张压"] = dt_split.str[0]
    df["收缩压"] = dt_split.str[1]

    def myFormat(x):
        if len(x.strip()) < 2:
            return '0' + x
        else:
            return x

    df['孕周4'] = df['孕周/周'].apply(lambda x: myFormat(x))

    df.sort_values(['身份证号码', '孕周4', '孕周/天'], inplace=True)
    df.to_excel(
        './excel/' + name + '_sort.xls', 'SQL Results')


def weightdiff():
    name = '2019.10.16BMI增长'
    df = pd.read_excel('./excel/' + name + '.xlsx', 'Sheet2')
    df['体重差'] = df.groupby('身份证号码')['体重'].apply(lambda i: i.diff(1))
    df['孕前体重差'] = df['体重'] - df['孕前体重新']

    def computeWeeb(week, day):
        if day < 4:
            return week
        else:
            return week + 1

    df['孕周/周'] = df.apply(lambda x: computeWeeb(x.week, x.day), axis=1)
    df.to_excel(
        './excel/' + name + '_new.xlsx', 'SQL Results')


def combineData():
    name = '原稿2019.10.19BMI'
    name2 = "参考表--2015-2018年妊娠期糖尿病"
    df = pd.read_excel('./excel/' + name + '.xlsx', 'SQL Results')
    df2 = pd.read_excel('./excel/' + name2 + '.xls', '查询结果')

    df3 = pd.merge(df, df2, left_on="ID", right_on="身份证号")
    df3.to_excel(
        './excel/' + name + '_combine.xlsx', 'SQL Results')


def repeatOneData():
    name = '原稿2019.10.19BMI_new'
    # df = pd.read_excel('./excel/' + name + '.xlsx', 'SQL Results')
    # print(df.groupby('ID').describe())

    dftemp = pd.read_excel('./excel/' + name + '.xlsx',
                           'SQL Results', usecols='B,X')
    newdata = {}
    print('read excel done')
    for row in dftemp.itertuples():
        # print(row)
        if not pd.isna(row[2]):
            if row[1] not in newdata.keys():
                newdata[row[1]] = row[2]

    print("repeatData step 1 complete")
    rowindex = 0
    for row1 in dftemp.itertuples():
        if row1[1] in newdata.keys():
            dftemp.loc[rowindex, '性别'] = newdata[row1[1]]
        rowindex += 1
        print(rowindex)
    print('step2 complete')
    dftemp.to_excel('./excel/' + name + '_repeatone.xlsx', 'SQL Results')
    print("repeatData steps complete")


def repeatData():
    name = '原稿2019.10.19BMI_new'
    # df = pd.read_excel('./excel/' + name + '.xlsx', 'SQL Results')
    # print(df.groupby('ID').describe())

    dftemp = pd.read_excel('./excel/' + name + '.xlsx',
                           'SQL Results', usecols='B,X,Y,Z,AA,AB,AC')
    newdata = {2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}}
    print('read excel done')
    for row in dftemp.itertuples():
        # print(row)
        if not pd.isna(row[2]):
            if row[1] not in newdata[2].keys():
                newdata[2][row[1]] = row[2]

        if not np.isnan(row[3]):
            if row[1] not in newdata[3].keys():
                newdata[3][row[1]] = row[3]
        if not np.isnan(row[4]):
            if row[1] not in newdata[4].keys():
                newdata[4][row[1]] = row[4]
        if not pd.isna(row[5]):
            if row[1] not in newdata[5].keys():
                newdata[5][row[1]] = row[5]
        if not pd.isna(row[6]):
            if row[1] not in newdata[6].keys():
                newdata[6][row[1]] = row[6]
        if not pd.isna(row[7]):
            if row[1] not in newdata[7].keys():
                newdata[7][row[1]] = row[7]
    print("repeatData step 1 complete")
    rowindex = 0
    for row1 in dftemp.itertuples():
        if row1[1] in newdata[2].keys():
            dftemp.loc[rowindex, '胎位'] = newdata[2][row1[1]]
        if row1[1] in newdata[3].keys():
            dftemp.loc[rowindex, '新生儿体重'] = newdata[3][row1[1]]
        if row1[1] in newdata[4].keys():
            dftemp.loc[rowindex, '新生儿身高'] = newdata[4][row1[1]]
        if row1[1] in newdata[5].keys():
            dftemp.loc[rowindex, '总评分1'] = newdata[5][row1[1]]
        if row1[1] in newdata[6].keys():
            dftemp.loc[rowindex, '总评分2'] = newdata[6][row1[1]]
        if row1[1] in newdata[7].keys():
            dftemp.loc[rowindex, '总评分3'] = newdata[7][row1[1]]
        rowindex += 1
        print(rowindex)
    print('step2 complete')
    dftemp.to_excel('./excel/' + name + '_repeat.xlsx', 'SQL Results')
    print("repeatData steps complete")
    # df.to_excel(
    #     './excel/' + name + '_repeat.xlsx', 'SQL Results')


def computeTimeToHour():
    name = '分娩镇痛总表'
    df = pd.read_excel('./other/' + name + '.xlsx',
                       sheet_name='2019年1月-9月镇痛组原始数据')

    def computeTime(x):
        print(x)
        if not isinstance(x, str):
            return x
        arr = x.split('小时')
        if arr[0].isdecimal():
            hour = int(arr[0])
        else:
            return x
        if arr[1].split('分')[0].isdecimal():
            minute = int(arr[1].split('分')[0])
            return hour + minute / 60
        else:
            return x

    df['第一产程_new'] = df['第一产程'].apply(lambda x: computeTime(x))
    df['第二产程_new'] = df['第二产程'].apply(lambda x: computeTime(x))
    df['第三产程_new'] = df['第三产程'].apply(lambda x: computeTime(x))
    df['总产程_new'] = df['总产程'].apply(lambda x: computeTime(x))
    df.to_excel(
        './other/' + name + '_new0.xlsx', '2019年1月-9月镇痛组原始数据')


def computeWeek():
    name = '分娩镇痛总表'
    df = pd.read_excel('./other/' + name + '.xlsx', '2019年1月-9月镇痛组原始数据')
    df['孕天/周'] = df['孕天\n'] / 7
    df['孕周总'] = df['孕天/周'] + df['孕周\n']

    df.to_excel(
        './other/' + name + '_week1.xlsx', '2019年1月-9月镇痛组原始数据')


# 方法主入口
if __name__ == '__main__':
    # inputWeight()
    # sortByWeek()
    # removeTheSameData()
    # weightdiff()
    # combineData()
    # repeatData()
    computeWeek()
