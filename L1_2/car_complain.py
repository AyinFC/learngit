#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# 根据request得到对应的BS对象
def get_page_content(request_url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(request_url, headers=header, timeout=10)
    content = html.text
    
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

# 通过BS来对象来提取当前对象的内容
def analysis(soup):
    # 找到完整的投诉框
    temp = soup.find('div', class_='tslb_b')
    #投诉编号	投诉品牌	投诉车系	投诉车型	问题简述	典型问题	投诉时间	投诉状态
    #先确定好内容格式，便于导出成csv
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    #找到所有的tr
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        #第一个tr没有td，其余的都有8个td
        #第一个tr是标题，其余tr才表示内容，每个都有8个类别的内容
        if len(td_list)>0:
            #解析各个字段的内容
            id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            #print(id, brand, car_model, type, desc, problem, datetime, status)
            temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp['problem'], temp['datetime'], temp['status'] = id, brand, car_model, type, desc, problem, datetime, status
            df = df.append(temp, ignore_index=True)
    return df
        

request_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
bs = get_page_content(request_url)
df = analysis(bs)
print(df)


# In[2]:


page_num = 10
base_url =  'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
for i in range(page_num):
    request_url = base_url + str(i+1) + '.shtml'
    soup = get_page_content(request_url)
    print('request_url:\n', request_url)
    df = analysis(soup)
    print('df:\n', df)
    result = result.append(df)
result.to_csv('car_complain.csv', index=False)
    

