# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:00:06 2020

@author: xiong
"""

import pandas as pd
import numpy as np
import math


def dealData():
    df = pd.read_excel('./分析汇总表.xlsx', 'Sheet1')
    df.head()
    df.fillna(method='pad')
    df.fillna('pad')
    df_g1 = df.groupby(['身份证号码', '出生日期'])
    df_g1.size()
    df_fat = df[df.BMI >= 30.0]
    df_fat.size()
    df_exception = df_fat[df_fat.Weight < df_fat.孕前体重]
    df_ex_g1 = df_exception.groupby(['身份证号码', '出生日期'])
    df_ex_g1.count()
    df_fat.to_excel('fat.xlsx')
    df_exception.to_excel('fat_exception.xlsx')
    df_exception.drop_duplicates(['身份证号码', '出生日期'], keep='last', inplace=True)
    df_exception.to_excel('fat_exception_dropduplicates.xlsx')
    df.drop_duplicates(['身份证号码', '出生日期'], keep='last', inplace=True)
    df.to_excel('drop_duplicates_all.xlsx')
  

dealData()
