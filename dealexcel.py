# encoding=utf8

import pandas as pd
import numpy as np


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
  for row1 in df.itertuples():
    if np.isnan(row1[2]) and row1[1] in newdata.keys():
      dfheight.loc[rowindex, '身高'] = newdata[row1[1]]
    rowindex += 1
  dfheight.to_excel('./excel/result.xls', 'SQL Results')
  print("getHeight steps complete")

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


def getHeightWithBMI():
  dfheight = pd.read_excel('./excel/test.xls', 'SQL Results', usecols='B,H,L')
  newdata = {}
  for row in dfheight.itertuples():
    # print(row)
    if not np.isnan(row[2]):
      if row[1] not in newdata.keys():
        newdata[row[1]] = row[2]
  print("getHeight step 1 complete")
  rowindex = 0
  for row1 in df.itertuples():
    if np.isnan(row1[2]) and row1[1] in newdata.keys():
      dfheight.loc[rowindex, '身高'] = newdata[row1[1]]
    rowindex += 1
  dfheight.to_excel('./excel/result.xls', 'SQL Results')
  print("getHeight steps complete")

def removeTheSameData():
  name = '2018年_sort'
  df = pd.read_excel('./excel/'+ name + '.xls', 'SQL Results')

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

# 方法主入口
if __name__ == '__main__':
    removeTheSameData()
    # sortByWeek()

