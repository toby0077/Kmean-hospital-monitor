# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:52:54 2018

@author: Administrator
kmean score ,计算kmean负面总分数
"""
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

df_total=pd.read_excel("商户_无缺失数据.xlsx")
df_goodCenters=pd.read_excel("good_centers.xlsx")
df_badCenters=pd.read_excel("bad_centers.xlsx")

list_goodNames=df_goodCenters.columns
list_badNames=df_badCenters.columns


#单个商户（整形医院）单个正面因子分数计算，row行的索引，column列的索引
def 单个商户_单个负面因子_score(row,column):
    商户名=df_total.ix[row,0]
    print("商户名:",商户名)
    负面因子名=list_badNames[column]
    print("负面因子名:",负面因子名)
    负面因子=df_total.ix[row,column+4]
    print("负面因子:",负面因子)
    此因子中心点=df_badCenters[负面因子名]
    差值=此因子中心点-负面因子
    差值_最小值=min(abs(差值))
    print("差值_最小值:",差值_最小值)
    #返回差值中最大值的索引index
    索引_最小值=差值[abs(差值)==差值_最小值].index[0]
    print("索引_最小值:",索引_最小值)
    if 索引_最小值==0:
        score_负面因子=3
    if 索引_最小值==1:
        score_负面因子=2
    if 索引_最小值==2:
        score_负面因子=1
    if 索引_最小值==3:
        score_负面因子=0  
  
    print("得分：",score_负面因子)
    return score_负面因子
    

#单个商户（整形医院）所有负面因子分数计算，row行的索引，column列的索引
def 单个商户_负面因子总分(row): 
    total_score=0
    商户名=df_total.ix[row,0]
    for column in range(len(list_goodNames)):
        score=单个商户_单个负面因子_score(row,column)
        total_score+=score
        column+=1
    print("商户名:",商户名)
    print("所有负面因子分数:",total_score)
    return total_score
    


#所有商户负面因子总分
def 所有商户_负面因子总分():
    所有商户数量=df_total['门店名称'].size
    for row in range(所有商户数量):
        商户名=df_total.ix[row,0]
        score=单个商户_负面因子总分(row)
        dict_商户_负面因子总分[商户名]=score
    return dict_商户_负面因子总分

#存储商户名和各自的正面因子总分
dict_商户_负面因子总分={}
dict_商户_负面因子总分=所有商户_负面因子总分()
  

#商户名列表
b=list(dict_商户_负面因子总分)
#商户名总分
c=list(dict_商户_负面因子总分.values())

data=pd.DataFrame({"商户名":b,"负面因子总分":c})  
data.to_excel("result_商户负面因子总分.xlsx")

'''
单个商户_所有正面因子_score=单个商户_所有正面因子_score(0)    

#单个商户（整形医院）分数计算
商户名=df_total.ix[0,0]
申请金额=df_total.ix[0,1]

申请金额中心点=df_goodCenters["申请金额"]
差值=申请金额中心点-申请金额
最小值=min(abs(差值))
#返回差值中最小值的索引index
index_min_minus=差值[abs(差值)==最小值].index[0]
score_申请金额=index_min_minus


批核金额=df_total.ix[0,2]
批核金额中心点=df_goodCenters["批核金额"]
差值=批核金额中心点-批核金额
最小值=min(abs(差值))
#返回差值中最小值的索引index
index_min_minus=差值[abs(差值)==最小值].index[0]
score_批核金额=index_min_minus



#测试数据
#name=df_total.values[0]
#字典，存储各个字段和分数
print(name)
['成都美莱医学美容医院' 29476700 15064900 0.939033758343591 0.04346739723121218
 0.008226571767497052 0.2905153099327857 0.10306198655713218
 0.039581777445855115 0.030619865571321882 0.03009259259259259
 0.039294105596298035]
type(name)
Out[4]: numpy.ndarray

df.ix[row,column]
df_total.ix[0,1]
Out[7]: 29476700

df_total.ix[0,0]
Out[8]: '成都美莱医学美容医院'

df_total.loc[df_total.index[0,"门店名称"]
'''
