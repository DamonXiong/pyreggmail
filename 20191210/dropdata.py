# encoding=utf8

import math

import numpy as np
import pandas as pd


def inputWeight(name):
    dfheight = pd.read_excel('./four/' + name + '.xls', 'SQL Results', usecols='B, J')
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
    dfheight.to_excel('./four/' + name + '_inputweight.xls', 'SQL Results')
    print("inputWeight steps complete")


def getBMI(name):
    df = pd.read_excel('./four/' + name + '.xls',
                       'SQL Results', usecols='B,K')
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
    df.to_excel('./four/' + name + '_bmi.xlsx', 'SQL Results')
    print("getBMI steps complete")


def removeTheSameData(name):
    df = pd.read_excel('./four/' + name + '.xls', 'SQL Results')

    df.drop_duplicates(['身份证号码', '孕周'], keep='last', inplace=True)
    df.to_excel(
        './four/' + name + '_drop.xls', 'SQL Results')


def sortByWeek(name):
    df = pd.read_excel('./four/' + name + '.xls', 'SQL Results')
    df['身高*身高'] = df.apply(lambda x: x['孕前体重_new'] / x['孕前体重指数_new'], axis=1)
    dt_split = df["孕周"].str.split('+')
    df["孕周/周"] = dt_split.str[0]
    df["孕周/天"] = dt_split.str[1]
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
        './four/' + name + '_sort.xls', 'SQL Results')


def computeWeek(name):
    df = pd.read_excel('./four/' + name + '.xls', 'SQL Results')

    # df['体重差'] = df.groupby('身份证号码')['体重'].apply(lambda i: i.diff(1))
    # df['孕前体重差'] = df['体重'] - df['孕前体重新']

    def computeWeeb(week, day):
        if week > 40:
            return week
        else:
            if day < 4:
                return week
            else:
                return week + 1

    df['孕周/周_new'] = df.apply(lambda x: computeWeeb(x['孕周/周'],
                                                    x['孕周/天']), axis=1)
    df.to_excel(
        './four/' + name + '_week.xls', 'SQL Results')


def combineData(name, totalname):
    df = pd.read_excel('./four/' + name + '.xls', 'SQL Results')
    df2 = pd.read_excel('./four/' + totalname + '.xls', '查询结果')

    df3 = pd.merge(df, df2, left_on="身份证号码", right_on="身份证号", how='left', indicator=True)
    df3.to_excel(
        './four/' + name + '_combine.xls', 'SQL Results')


def repeatData():
    name = '原稿2019.10.19BMI_new'
    # df = pd.read_excel('./excel/' + name + '.xlsx', 'SQL Results')
    # print(df.groupby('ID').describe())

    dftemp = pd.read_excel('./twice/' + name + '.xlsx',
                           'SQL Results', usecols='B,V')
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
            dftemp.loc[rowindex, '分娩方式'] = newdata[row1[1]]
        rowindex += 1
        print(rowindex)
    print('step2 complete')
    dftemp.to_excel('./twice/' + name + '_repeat.xlsx', 'SQL Results')
    print("repeatData steps complete")
    # df.to_excel(
    #     './excel/' + name + '_repeat.xlsx', 'SQL Results')


def getGroupData():
    name = '2018年_combine'
    df = pd.read_excel('./four/' + name + '.xlsx',
                       'SQL Results', usecols='A,B')
    print('read done')
    df_group = df.groupby('INDEX').aggregate(lambda x: list(x)).reset_index()
    print('group done')
    df_group.to_excel('./four/' + name + '_groupbyapply.xlsx')


def combineHeight(name, totalname):
    df = pd.read_excel('./three/' + name + '.xls', 'Sheet1')
    df2 = pd.read_excel('./three/' + totalname + '.xlsx',
                        'SQL Results', usecols='D,K')

    newdata = {}
    print('read excel done')
    for row in df2.itertuples():
        # print(row)
        if not pd.isna(row[2]):
            if row[1] not in newdata.keys():
                newdata[row[1]] = row[2]
    print("repeatData step 1 complete")
    rowindex = 0
    for row1 in df.itertuples():
        if row1[1] in newdata.keys():
            df.loc[rowindex, '身高'] = newdata[row1[1]]
        rowindex += 1
        print(rowindex)
    print('step2 complete')
    print("repeatData steps complete")
    df.to_excel(
        './three/' + name + '_combine.xlsx', 'SQL Results')


def duplicatedCount(name):
    df = pd.read_excel('./four/' + name + '.xls',
                       'SQL Results')

    dup = df.duplicated(['身份证号码', '孕周']).reset_index()
    dup.to_excel(
        './four/' + name + '_duplicatedcount.xls', 'SQL Results')


def sortByBirth(name):
    df = pd.read_excel('./four/' + name + '.xls', 'SQL Results')

    df.sort_values(['身份证号码', '出生日期', '孕周'], inplace=True)
    df.to_excel(
        './four/' + name + '_sortbybirth.xls', 'SQL Results')


def computeHeight(name):
    df = pd.read_excel('./five/' + name + '.xls', 'Sheet1')
    df['身高计算'] = df['身高*身高'].apply(lambda x: math.sqrt(x))

    def qusui(x):
        if isinstance(x, str):
            return x.split('岁')[0]
        else:
            return x

    df['年龄去岁'] = df['年龄'].apply(lambda x: qusui(x))

    df.to_excel(
        './five/' + name + '_computeheight.xls', 'Sheet1')


def inputBabyGender():
    # df = pd.read_excel('./six/分析汇总表2.xlsx', 'Sheet1')
    dftotal = pd.read_excel('./six/input.xlsx', 'Sheet1')

    def qusui(x):
        if isinstance(x, str):
            return x.split('岁')[0]
        else:
            return x

    dftotal['年龄去岁'] = dftotal['年龄'].apply(lambda x: qusui(x))

    dftotal.to_excel(
        './six/qusui.xlsx', 'Sheet1')


# 方法主入口
if __name__ == '__main__':
    df = pd.read_excel('./20191210/身高缺失2019.12.22(处理完成).xlsx', 'Sheet1')
    df2 = pd.read_excel('./20191210/2013-2018汇总表.xls', '查询结果')
    # df.drop_duplicates(['身份证号码', '出生日期'], keep='last', inplace=True)

    df3 = pd.merge(df, df2, on=['身份证号码', '出生日期'])
    df3.to_excel(
        './20191210/身高缺失2019.12.22(处理完成)_merge.xlsx', 'Sheet1')
