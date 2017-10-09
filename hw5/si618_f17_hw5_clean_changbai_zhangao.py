#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:47:37 2017

@author: liuchangbai
"""

import pandas as pd
import numpy as np


#df = pd.read_csv("si618_f17_hw5_batch_result_changbai_zhangao.csv", sep = ',',)
df = pd.read_csv("si618_f17_hw5_batch_result_changbai_zhangao.csv", sep = ',')

group = df.groupby(by = 'HITId')

a = group['Answer.a'].count()
b = group['Answer.b'].count()
c = group['Answer.c'].count()
d = group['Answer.d'].count()
e = group['Answer.e'].count()
f = group['Answer.f'].count()


temp = df.drop_duplicates(['HITId'])
lab = pd.read_csv('si618_f17_lab5_random_sample_100_comments_zhangao_changbai.csv')


# Result DataFrame
#result_df = pd.DataFrame(columns = ['HITId', 'pagename', 'post_id', 'comment_id','answer_1',
#                                    'answer_2','answer_3','answer_4','answer_5','answer_6'],
#                        index = range(0,100))
result_df = pd.DataFrame(index = range(0,100))

#result_df['HITId'] = temp['HITId'].values
result_df['pagename'] = lab['pagename'].values
result_df['post_id'] = lab['post_id'].values
result_df['comment_id'] = lab['comment_id'].values
result_df['answer_1'] = a.values
result_df['answer_2'] = b.values
result_df['answer_3'] = c.values
result_df['answer_4'] = d.values
result_df['answer_5'] = e.values
result_df['answer_6'] = f.values

result_df.replace(np.nan, 0)

result_df.to_csv('si618_f17_hw5_cleaned_data_changbai_zhangao.csv', index = False)
