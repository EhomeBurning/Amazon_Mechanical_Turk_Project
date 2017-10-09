
import csv
import re
import random
from facepy import GraphAPI
from urllib.request import urlopen
import pandas as pd


graph = GraphAPI("534027846937600|ThipY0e-gM7aK6qN319cIhOIuKY")

# Get my latest posts
doc=graph.get('nytimes/posts?fields=message,from,comments{message,from,comments{message,from,id,comments{message,from,id}},id},id&until=2017-09-26&since=2017-09-20')


emoji_pattern = re.compile(
    u"[\U00010000-\U0001ffff]|"
    u"[\u2764]"
    "+", flags=re.UNICODE)
def remove_emoji(text):
    return emoji_pattern.sub(r'', text)



data=doc.get('data',None)
comments=[]
for i in range(len(data)):
    post_id=data[i].get('from',None)
    comments.append(("nytimes",remove_emoji(data[i].get('message', None)),data[i].get('id',None),post_id.get('id',None)))
    nest1=data[i].get('comments',None)
    nest=nest1.get('data',None)
    for i in range(len(nest)):
        com=remove_emoji(nest[i].get('message', None))
        comment_id=nest[i].get('id', None)
        poster=nest[i].get('from', None)
        post_id=poster.get('id',None)
        comments.append(('nytimes',com,comment_id,post_id))
        nest2 = nest[i].get('comments', None)
        if nest2 != None:
            nest3= nest2.get('data', None)
            for i in range(len(nest3)):
                com = remove_emoji(nest3[i].get('message', None))
                comment_id = nest3[i].get('id', None)
                poster = nest3[i].get('from', None)
                post_id = poster.get('id', None)
                comments.append(('nytimes', com, comment_id, post_id))
                nest4 = nest3[i].get('comments', None)
                if nest4 != None:
                    nest5 = nest4.get('data', None)
                    for i in range(len(nest5)):
                        com = remove_emoji(nest5[i].get('message', None))
                        comment_id = nest5[i].get('id', None)
                        poster = nest5[i].get('from', None)
                        post_id = poster.get('id', None)
                        comments.append(('nytimes', com, comment_id, post_id))



sample=random.sample(comments, 100)


with open('si618_f17_lab5_number_of_comments_zhangao_changbai.txt','w') as question2:
    question2.write(str(len(comments)))



#header = ['pagename','comment','comment_id','post_id']
sampleFile = "si618_f17_lab5_random_sample_100_comments_zhangao_changbai.csv"
#with open(sampleFile, 'w') as f:
#    f_csv = csv.writer(f,quoting=csv.QUOTE_ALL)
#    f_csv.writerow(header)
##    for i in range(0,len(sample)):
##        f_csv.writerows(sample[i])
#    f_csv.writerows(sample)

df = pd.DataFrame(sample)
df.columns = ['pagename','comment','comment_id','post_id']
df = df[['pagename','post_id','comment_id','comment']]
df.to_csv(sampleFile,index = False)


'''
sampleFile = "si618_f17_lab5_random_sample_100_comments_zhangao_changbai.csv"
with open(sampleFile, 'w') as f:
    wr = csv.writer(f, delimiter = '\n')
    wr.writerow(",".join(['page_name','comment', 'comment_id','post_id']))
    for item in sample:
        wr.writerow('nytimes' + ', ' + item[0] + ', ' + item[1] + ', ' + item[2])
'''
