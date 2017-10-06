# Amazon_Mechanical_Turk_Project
hw5+lab5

import re
import random
from facepy import GraphAPI
from urllib.request import urlopen



graph = GraphAPI("EAACEdEose0cBAHzN8KlGMiY3NDMTnaZCquTUB207EKxnvIXsF91ZBbWpZCLUwuaODFZCZApUbYok6LIydVZBsQnl35NLI0sUbkqrvh4vYhq3D64E2Rhh6b3BfIXWg9gRqZAwRvcs6BW5bda0D5b4fLwUKJJysaiLokukgcJFTXVN9DipfzdaZB4wrh9EEZCuP5AbjlkcZAczfcjwZDZD")

# Get my latest posts
doc=graph.get('nytimes/posts?fields=id,message,comments,created_time,from&since=2017-09-20&until=2017-09-26')
data=doc.get('data',None)
comments=[]
cid=[]
pid=[]

emoji_pattern = re.compile(
    u"[\U00010000-\U0001ffff]|"
    u"[\u2764]"
    "+", flags=re.UNICODE)
def remove_emoji(text):
    return emoji_pattern.sub(r'', text)




for i in range(len(data)):
    comments.append(remove_emoji(data[i].get('message',None)))
    cid.append(data[i].get('id',None))
    post_id=data[i].get('from',None)
    pid.append(post_id.get('id',None))
    nest1=data[i].get('comments',None)
    nest=nest1.get('data',None)
    for i in range(len(nest)):
        com=remove_emoji(nest[i].get('message', None))
        comment_id=nest[i].get('id', None)
        poster=nest[i].get('from', None)
        post_id=poster.get('id',None)
        comments.append(com)
        cid.append(comment_id)
        pid.append(post_id)


list=(range(len(comments)))
sample=random.sample(list, 100)


with open('si618_f17_lab5_number_of_comments_zhangao_changbai.txt','w') as question2:
    question2.write(str(len(comments)))

with open('si618_f17_lab5_random_sample_100_comments_zhangao_changbai.csv','w') as question1:
    question1.write('comments,comment_id,post_id\n')
    for i in sample:
        question1.write(comments[i]+','+cid[i]+','+pid[i]+'\n')
