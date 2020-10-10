# encoding=utf8

import numpy as np
import pandas as pd


def repeatData():
    # dftemp = pd.read_excel('./20200101/分析汇总表2019.12.31.xlsx', 'Sheet1')
    # df = dftemp.groupby(['身份证号码', '出生日期']).apply(
    #     lambda t: t[t['胎龄周'] != t['week'].max()])

    df = pd.read_excel('./20200101/分析汇总表20200104copy_input.xlsx', 'Sheet1')
    max_df = df.groupby(['身份证号码'])['week'].max().reset_index()

    def inputTLZ(x):
        if x['胎龄周_new'] == 0:
            y = max_df.loc[(max_df["身份证号码"] == x['身份证号码'])].reset_index()
            if len(y['week']) == 1:
                return y['week'][0]
            else:
                return x['胎龄周_new']
        else:
            return x['胎龄周_new']

    df['胎龄周_new_twice'] = df.apply(lambda x: inputTLZ(x), axis=1)
    df.to_excel(
        './20200101/分析汇总表20200104copy_input_complete.xlsx', 'Sheet1')
    print("input steps complete")


def mergeinof():
    df = pd.read_excel('./20200101/分析汇总表20200104copy.xlsx', 'Sheet1')
    df2 = pd.read_excel('./20191210/2013-2018汇总表.xls', '查询结果')
    print('read done')
    df.drop_duplicates(['身份证号码', '出生日期'], keep='last', inplace=True)
    print('drop done')
    df = df.loc[((df["新生儿体重"] == 0) | (df["新生儿身高"] == 0))].reset_index()

    print('get done')
    df_res = pd.merge(df, df2, on=['身份证号码', '出生日期'], how='left')
    # df2 = df.loc[(df["新生儿体重"] == 0 | df["新生儿身高"] == 0)].reset_index()

    print('merge done')
    df_res.to_excel(
        './20200101/分析汇总(处理完成).xlsx', 'Sheet1')
    # df2.to_excel(
    #     './20200101/缺失2020.01.03(处理完成).xlsx', 'Sheet1')


# mergeinof()

# repeatData()


def inputHeight():
    dfheight = pd.read_excel('./20200101/身高体重.xls', 'SQL Results')
    df = pd.read_excel(
        './20200101/分析汇总表20200104copy_input_complete.xlsx', 'Sheet1')
    for i, row in df.iterrows():
        if np.isnan(row['新生儿体重']) or row['新生儿体重'] == 0:
            serie = dfheight.loc[dfheight['姓名'] == row['姓名']]['体重']
            if len(serie.values) > 0:
                # print(serie)
                df.loc[i, '新生儿体重'] = serie.values[0]
        if np.isnan(row['新生儿身高']) or row['新生儿身高'] == 0:
            serie = dfheight.loc[dfheight['姓名'] == row['姓名']]['身高']
            if len(serie.values) > 0:
                # print(serie)
                df.loc[i, '新生儿身高'] = serie.values[0]
    df.to_excel(
        './20200101/分析汇总表20200104copy_input_complete(inputheight)_done.xlsx', 'Sheet1')
    print("getHeight steps complete")


inputHeight()
