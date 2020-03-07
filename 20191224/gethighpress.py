# encoding=utf8

import pandas as pd
import numpy as np
import math

def inputHighPress():
  df = pd.read_excel(
      './20191224/2019.12.24--分析汇总表(inputheight)_done.xlsx', 'Sheet1')
  for i, row in df.iterrows():
    if row['week'] > 20 and row['收缩压'] >= 140 and row['舒张压'] >= 90:
        df.loc[i, '高血压'] = '是'
  df.to_excel('./20191224/2019.12.24--分析汇总表(inputhighpress).xlsx', 'Sheet1')
  print("getHeight steps complete")


inputHighPress()

