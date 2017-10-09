#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:32:56 2017

@author: liuchangbai
"""



import pandas as pd

df = pd.read_csv("si618_f17_hw5_cleaned_data_changbai_zhangao.csv")


result_list = []
# Question1 : For what fraction of comments do all three workers agree whether or not there is some sort of personal attack? 
def question1(row):
    temp = row[3:9]
    nonzero = temp.nonzero()[0]
    n = temp.iloc[nonzero]
    if len(n) == 1:
        return 1
    else:
        return 0

df['question1'] = df.apply(lambda x: question1(x), axis=1)
result1 = df['question1'].mean()
result_list.append(result1)


# Question2 : How often do at least two workers believe there is some sort of a personal attack? 
def question2(row):
    temp = row[3:9]
    nonzero = temp.nonzero()[0]
    n = temp.iloc[nonzero]
    if len(n) <= 2:
        return 1
    else:
        return 0

df['question2'] = df.apply(lambda x: question2(x), axis=1)
result2 = df['question2'].mean()
result_list.append(result2)

# Question3 : 1.    How often does at least one worker believe there is some sort of a personal attack? Report the fraction.
def question3(row):
    temp = row[3]
    if temp > 0:
        return 1
    else:
        return 0

df['question3'] = df.apply(lambda x: question3(x), axis=1)
result3 = df['question3'].mean()
result_list.append(result3)

#print(result_list)


file = open("si618_f17_hw5_analysis_output_changbai_zhangao.txt","w")
for i in result_list:
    file.write(str(i))
    file.write('\n')

file.close()


