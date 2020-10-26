import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
#from selenium import webdriver

# driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
# driver.get("https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A")

url = "https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A"
res = requests.get(url=url)
soup = BeautifulSoup(res.content, features='lxml')


def DBinsert(data):
    db_url = 'mongodb://192.168.0.134:8088/'

    with MongoClient(db_url) as client:
        kdb = client['kstartup']
       
        infor = kdb.kdbCollection.insert_one(data)

def kdb():

    #기간 진배꺼 # due_enddate
    terms = soup.select('h4 > span[class*="ann_list_day"]')
    # for term in terms:
    #     print(term.text)



    
    #카테고리 진배꺼 #카테고리 category
    cates = soup.select('h4 > span[class*="ann_list_group"]')
    # for cate in cates:
    #     print(cate.text)


    

    #li들 뽑아내기....진배옹의 가르침
    li1_text, li2_text, li3_text= [], [], []
    ul_tags = soup.find_all('ul', class_='ann_list_info m0')
    for ul in ul_tags:
        li_tags = []
        for li in ul.find_all('li'):
            li_tags.append(li.text)
        li1_text.append(li_tags[0])
        li2_text.append(li_tags[1])
        li3_text.append(li_tags[2].split()[1])
    #print(li1_text)


    #타이틀 완료 #타이틀 title
    titles= soup.select("li > h4 > a")
    # for title in titles:
    #     print(title.text)


    

    for cate, term, title, li11_text, li22_text, li33_text in zip(cates, terms, titles, li1_text, li2_text, li3_text):
        #print(cate.text, term.text, title.text, li1_text, li2_text, li3_text)


        data = {'category':cate.text, 'Term':term.text, 'post_title':title.text.strip(), 'sorting':li11_text, 'organization':li22_text, 'due_enddate':li33_text}
        print(data)
        DBinsert(data)



if __name__ == "__main__":
    kdb()
