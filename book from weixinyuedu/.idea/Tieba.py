import re 
import csv
#打开数据
with open('source.txt','r',encoding='UTF-8') as f:
    source = f.read()
    
result_list = []
username_list = re.findall('username="(.*?)"',source,re.S)
content_list = re.findall('clearfix" style="display:;">(.*?)<',source,re.S)
reply_time_list = re.findall('&quot;(2022.*?)&quot',source,re.S)


for i in range(len(username_list)):
    result = {'username':username_list[i],
              'content':content_list[i],
              'reply_time':reply_time_list[i]
              }
    result_list.append(result)

with open(tieba.csv,'w',encoding='UTF-8') as f:
    writer = csv.DictWriter(f,fieldnames=['username','content','reply_time'])
    writer.writeheader()
    writer.writerows(result_list)