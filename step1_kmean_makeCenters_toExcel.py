# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:50:05 2018

@author: Administrator

此脚本生成各个维度的四个中心点，kmean算法
"""

from sklearn.cluster import KMeans
import pandas as pd

df_good=pd.read_excel("正面因子.xlsx")
df_bad=pd.read_excel("负面因子.xlsx")
#df_concat=pd.DataFrame()

#所有变量列表
list_good_columns=list(df_good.columns)
list_bad_columns=list(df_bad.columns)


#获取一个字段的中心点，存储数据结构为df,kmean计算要用df数据结构，不用series数据结构
def Get_single_centers(df,column_name):
    series1=df[column_name]
    series2=series1.dropna()
    df=pd.DataFrame(series2)
    kmeans = KMeans(n_clusters=4, random_state=0).fit(df)
    centers=kmeans.cluster_centers_
   # print(centers)
    #df_centers=pd.DataFrame(data=centers,index=index,columns=column_name)
    df_centers=pd.DataFrame(centers)
    return df_centers

#获取所有字段的中心点，存储数据结构为df,kmean计算要用df数据结构，不用series数据结构
def Get_all_centers(df,list_columns):
    df_concat=pd.DataFrame()
    for column_name in list_columns:
        #print("column name",column_name)
        df_single_centers=Get_single_centers(df,column_name)
        #print(df_single_centers)
        df_concat=pd.concat([df_concat,df_single_centers],axis=1)
       
        #print("df_concat",df_concat)
    return df_concat
        

#把dataframe结果写入excel
def Write_excel(df,list_columns,excelName):
    df_all_centers=Get_all_centers(df,list_columns)
    values=df_all_centers.values
    #对numpy array排序
    values.sort(axis=0, kind='quicksort', order=None)
    #生成新的DataFrame数据结构，data要用array数据结构
    df_sort=pd.DataFrame(data=values,columns=list_columns)

    #保存结果
    df_sort.to_excel(excelName)

Write_excel(df_good,list_good_columns,"good_centers.xlsx")
Write_excel(df_bad,list_bad_columns,"bad_centers.xlsx")

