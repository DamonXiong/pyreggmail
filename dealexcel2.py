# encoding=utf8

import pandas as pd
import numpy as np
import math

def inputHeight(name):
  dfheight = pd.read_excel('./four/'+ name + '.xls', 'SQL Results', usecols='B,H,I')
  newdata = {2:{}, 3:{}}
  for row in dfheight.itertuples():
    # print(row)
    if not np.isnan(row[2]):
      if row[1] not in newdata[2].keys():
        newdata[2][row[1]] = row[2]

    if not np.isnan(row[3]):
      if row[1] not in newdata[3].keys():
        newdata[3][row[1]] = row[3]
  print("getHeight step 1 complete")
  rowindex = 0
  for row1 in dfheight.itertuples():
    if np.isnan(row1[2]) and row1[1] in newdata[2].keys():
      dfheight.loc[rowindex, '身高'] = newdata[2][row1[1]]
    if np.isnan(row1[3]) and row1[1] in newdata[3].keys():
      dfheight.loc[rowindex, '体重指数'] = newdata[3][row1[1]]
    rowindex += 1
  dfheight.to_excel('./four/'+ name + '_getHeight.xls', 'SQL Results')
  print("getHeight steps complete")


def inputWeight(name):
  dfheight = pd.read_excel('./four/'+ name + '.xls', 'SQL Results', usecols='B, J')
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
  df = pd.read_excel('./four/'+ name + '.xls', 'SQL Results')

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

  df3 = pd.merge(df, df2,  left_on="身份证号码",  right_on="身份证号", how='left', indicator=True)
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
  # dfto = dftotal.drop_duplicates('身份证号')
  # df4 = pd.merge(df, dftotal,  left_on="身份证号码",  right_on="身份证号", how='left', indicator=True)

  # for idx in range(0, len(df)):
  #     if pd.isnull(df.loc[idx]['性别']):
  #       print(idx)
  #       total = dfto.loc[dfto['身份证号'] == df.loc[idx]['身份证号码']]
  #       if len(total['年龄'].values) > 0:
  #         df.loc[idx,'年龄'] = total['年龄去岁'].values[0]
  #       if len(total['职业'].values) > 0:
  #         df.loc[idx, '职业'] = total['职业'].values[0]
  #       if len(total['分娩方式'].values) > 0:
  #         df.loc[idx, '分娩方式'] = total['分娩方式'].values[0]
  #       if len(total['第一产程'].values) > 0:
  #         df.loc[idx, '第一产程'] = total['第一产程'].values[0]
  #       if len(total['第二产程'].values) > 0:
  #         df.loc[idx, '第二产程'] = total['第二产程'].values[0]
  #       if len(total['第三产程'].values) > 0:
  #         df.loc[idx, '第三产程'] = total['第三产程'].values[0]
  #       if len(total['总产程'].values) > 0:
  #         df.loc[idx, '总产程'] = total['总产程'].values[0]
  #       if len(total['前羊水'].values) > 0:
  #         df.loc[idx, '前羊水'] = total['前羊水'].values[0]
  #       if len(total['性别'].values) > 0:
  #         df.loc[idx, '性别'] = total['性别'].values[0]
  #       if len(total['胎位'].values) > 0:
  #         df.loc[idx, '胎位'] = total['胎位'].values[0]
  #       if len(total['出生日期'].values) > 0:
  #         df.loc[idx, '出生日期'] = total['出生日期'].values[0]
  #       if len(total['总评分1'].values) > 0:
  #         df.loc[idx, '总评分1'] = total['总评分1'].values[0]
  #       if len(total['总评分2'].values) > 0:
  #         df.loc[idx, '总评分2'] = total['总评分2'].values[0]
  #       if len(total['总评分3'].values) > 0:
  #         df.loc[idx, '总评分3'] = total['总评分3'].values[0]
  #       if len(total['胎龄周'].values) > 0:
  #         df.loc[idx, '胎龄周'] = total['胎龄周'].values[0]
  #       if len(total['产别P'].values) > 0:
  #         df.loc[idx, '产别P'] = total['产别P'].values[0]
  #       if len(total['产别G'].values) > 0:
  #         df.loc[idx, '产别G'] = total['产别G'].values[0]
  #       if len(total['新生儿体重'].values) > 0:
  #         df.loc[idx, '新生儿体重'] = total['新生儿体重'].values[0]
  #       if len(total['新生儿身高'].values) > 0:
  #         df.loc[idx, '新生儿身高'] = total['新生儿身高'].values[0]

  dftotal.to_excel(
      './six/qusui.xlsx', 'Sheet1')

# 方法主入口
if __name__ == '__main__':
    inputBabyGender()
    #Step1 填充数据
    # name = "2013年"
    # totalName = "2013-2014妊娠期糖尿病"
    # inputWeight(name)
    # inputHeight(name)
    # getBMI(name)
    # name = "2014年"
    # inputWeight(name)
    # inputHeight(name)
    # getBMI(name)
    # name = "2015年"
    # inputWeight(name)
    # inputHeight(name)
    # getBMI(name)
    # name = "2016年"
    # inputWeight(name)
    # inputHeight(name)
    # getBMI(name)
    # name = "2017年"
    # inputWeight(name)
    # inputHeight(name)
    # getBMI(name)
    # name = "2018年"
    # inputWeight(name)
    # inputHeight(name)
    # getBMI(name)

    # Step3.统计重复内容index后去重
    # name = "2013年_sort_week_drop_combine_sortbybirth"
    # duplicatedCount(name)
    # removeTheSameData(name)
    # name += "_drop"
    # computeHeight(name)
    # name = "2014年_sort_week_drop_combine_sortbybirth"
    # duplicatedCount(name)
    # removeTheSameData(name)
    # name += "_drop"
    # computeHeight(name)
    # name = "2015年_sort_week_drop_combine_sortbybirth"
    # duplicatedCount(name)
    # removeTheSameData(name)
    # name += "_drop"
    # computeHeight(name)
    # name = "2016年_sort_week_drop_combine_sortbybirth"
    # duplicatedCount(name)
    # removeTheSameData(name)
    # name += "_drop"
    # computeHeight(name)
    # name = "2017年_sort_week_drop_combine_sortbybirth"
    # duplicatedCount(name)
    # removeTheSameData(name)
    # name += "_drop"
    # computeHeight(name)
    # name = "2018年_sort_week_drop_combine_sortbybirth"
    # duplicatedCount(name)
    # removeTheSameData(name)
    # name += "_drop"
    # computeHeight(name)

    # Step 2获取需要值，排序，去重，合并
    # name = "2013年"
    # totalName = "2013-2014妊娠期糖尿病"
    # sortByWeek(name)
    # name += "_sort"
    # computeWeek(name)
    # name += "_week"
    # removeTheSameData(name)
    # name +="_drop"
    # combineData(name, totalName)
    # name +="_combine"
    # sortByBirth(name)

    # name = "2014年"
    # sortByWeek(name)
    # name += "_sort"
    # computeWeek(name)
    # name += "_week"
    # removeTheSameData(name)
    # name += "_drop"
    # combineData(name, totalName)
    # name +="_combine"
    # sortByBirth(name)

    # name = "2015年"
    # totalName = "参考表--2015-2018年妊娠期糖尿病"
    # sortByWeek(name)
    # name += "_sort"
    # computeWeek(name)
    # name += "_week"
    # removeTheSameData(name)
    # name += "_drop"
    # combineData(name, totalName)
    # name +="_combine"
    # sortByBirth(name)

    # name = "2016年"
    # totalName = "参考表--2015-2018年妊娠期糖尿病"
    # sortByWeek(name)
    # name += "_sort"
    # computeWeek(name)
    # name += "_week"
    # removeTheSameData(name)
    # name += "_drop"
    # combineData(name, totalName)
    # name +="_combine"
    # sortByBirth(name)

    # name = "2017年"
    # totalName = "参考表--2015-2018年妊娠期糖尿病"
    # sortByWeek(name)
    # name += "_sort"
    # computeWeek(name)
    # name += "_week"
    # removeTheSameData(name)
    # name += "_drop"
    # combineData(name, totalName)
    # name +="_combine"
    # sortByBirth(name)

    # name = "2018年"
    # totalName = "参考表--2015-2018年妊娠期糖尿病"
    # sortByWeek(name)
    # name += "_sort"
    # computeWeek(name)
    # name += "_week"
    # removeTheSameData(name)
    # name += "_drop"
    # combineData(name, totalName)
    # name +="_combine"
    # sortByBirth(name)

