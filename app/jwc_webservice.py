from urllib import parse,request
import json
from flask import Flask, jsonify
from flask import request
import urllib
from bs4 import BeautifulSoup
from app import app
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
import requests
import random
import socket
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0


@app.route('/main_fun', methods=['GET','POST'])
def main_fun():
    if request.method == 'POST':
<<<<<<< HEAD
<<<<<<< HEAD
        dic1 = request.form
        print(dic1.to_dict())
=======
<<<<<<< HEAD
        dic1 = request.form
        print(dic1.to_dict())
=======
        #socket.setdefaulttimeout(3)
        dic1 = request.form
        #print(dic1.to_dict())
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
        dic1 = request.form
        print(dic1.to_dict())
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        dic2 = dic1.to_dict()
        dic3 = parse.urlencode (dic2).encode (encoding='utf-8')
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/x-www-form-urlencoded"}
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        url = 'http://59.72.194.12:8086/index.aspx'
        req = urllib.request.Request (url=url, data=dic3, headers=header_dict)
        res = urllib.request.urlopen (req)
        final_data = res.read ( ).decode ('utf-8')
        print (final_data)
        return final_data
        #return jsonify(dic1)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        #iplist = ['http://59.72.194.12:8086/index.aspx','http://59.72.194.19:8081/index.aspx','http://59.72.194.19:9001/index.aspx','http://59.72.194.12:9099/index.aspx']
        #url = random.choice(iplist)
        url = 'http://59.72.194.21:9099/index.aspx'
        req = urllib.request.Request (url=url, data=dic3, headers=header_dict)
        res = urllib.request.urlopen (req)
        final_data = res.read ( ).decode ('utf-8')
        #print (final_data)
        res.close()
        return final_data
        #return jsonify(dic1) 
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0

@app.route('/table', methods=['GET','POST'])
def get_table():
    if request.method == 'POST':
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        username = request.form.get['studentNo']
        pwd = request.form.get['password']
        from app import login_cookie
        cookiee = login_cookie.main ( )
        cookies = cookiee.get_cookie (username, pwd)
        url2 = 'http://59.72.194.13/TimetableSearch/TimetableSerachStudentSingleSpan.aspx'
        r = urllib.requests.get (url2, cookies=cookies)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        username = request.form.get('studentNo')
        pwd = request.form.get('password')
        from app import login_cookies_new
        cookiee = login_cookies_new.main ( )
        cookies = cookiee.get_cookie (username, pwd)
        url2 = 'http://59.72.194.13/TimetableSearch/TimetableSerachStudentSingleSpan.aspx'
        r = requests.get (url2, cookies=cookies)
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        soup = BeautifulSoup (r.content, 'html.parser', from_encoding='utf-8')
        tables = soup.findAll ('table', id='TableLCRoomOccupy')
        tab = tables[0]
        # print(tab)
        cont = tab.findAll ('tr')
        # print(cont[1])
        # for td in tr.find_all('td'):
        lists = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        # print(cont[1].findAll('td'))
        for i in range (1, len (tab.findAll ('tr'))):
            for td in cont[i].find_all ('td'):
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
                if i == 1:
                    list1.append (td.text)
                if i == 2:
                    list2.append (td.text)
                if i == 3:
                    list3.append (td.text)
                if i == 4:
                    list4.append (td.text)
                if i == 5:
                    list5.append (td.text)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
             textx = td.getText('\n')
             listx = textx.split('\n')
             #print(listx)
             dic_lesson = {}
             if len(listx) == 1:
                pass
             else:
                dic_lesson['name'] = listx[0]
                dic_lesson['tec'] = listx[1]
                dic_lesson['loc'] = listx[2]
                dic_lesson['time'] = listx[3]
                dic_lesson['class'] = listx[5]
             if i == 1:
                list1.append (dic_lesson)
             if i == 2:
                list2.append (dic_lesson)
             if i == 3:
                list3.append (dic_lesson)
             if i == 4:
                list4.append (dic_lesson)
             if i == 5:
                list5.append (dic_lesson)
        del list1[0]
        del list2[0]
        del list3[0]
        del list4[0]
        del list5[0]
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
                    # list = []
                    # list.append(td.text)
                    # print(td.get_text())
                    # print(list)
        lists.append (list1)
        lists.append (list2)
        lists.append (list3)
        lists.append (list4)
        lists.append (list5)
        # print (lists)
        return jsonify (lists)


@app.route('/books' , methods=['GET','POST'])
def get_book():
    if request.method == 'POST':
<<<<<<< HEAD
<<<<<<< HEAD
        book_name = request.form.get['book_name']
=======
<<<<<<< HEAD
        book_name = request.form.get['book_name']
=======
        book_name = request.form.get('book_name')
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
        book_name = request.form.get['book_name']
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        from app import book_main
        book = book_main.main ( )
        content = book.get_content (book_name)
        list1 = book.get_booklist (content)
        list2 = book.get_booklistdetail (content)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        list3 = book.get_index (list1)
        list4 = book.get_json (list1, list2)
        print (list4)
        from spider_book import global_ls
        global_ls.global_list = list3
        return jsonify (list4)

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        #list3 = book.get_index (list1)
        list4 = book.get_json (list1, list2)
        #print (list4)
        #from spider_book import global_ls
        #global_ls.global_list = list3
        return jsonify (list4)

@app.route('/pagebooks' , methods=['GET','POST'])
def get_pagebook():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        page_num = request.form.get('page_num')
        from app import book_main
        book = book_main.main ( )
        content = book.get_numpage (book_name,page_num)
        list1 = book.get_booklist (content)
        list2 = book.get_booklistdetail (content)
        #list3 = book.get_index (list1)
        list4 = book.get_json (list1, list2)
        #print (list4)
        #from spider_book import global_ls
        #global_ls.global_list = list3
        return jsonify (list4)
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0

@app.route('/book_content',methods=['GET','POST'])
def get_book_content():
    if request.method == 'POST':
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
=======
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
        book_index = request.form.get['book_index']
        from app import book_main
        book = book_main.main ()
        print (book_index)
        content = book.get_detail (book_index)
        return jsonify (content)



if __name__ == "__main__":

<<<<<<< HEAD
<<<<<<< HEAD
     app.run (debug=True)
=======
     app.run (debug=True)
=======
        book_index = request.form.get('book_index')
        from app import book_main
        book = book_main.main ()
        #print (book_index)
        content = book.get_detail (book_index)
        return jsonify (content)

@app.route('/book_login',methods=['GET','POST'])
def get_booklogin():
    if request.method == 'POST':
        stnumber = request.form.get('stnumber')
        passwd = request.form.get('password')
        from app import clear_system
        book = clear_system.main ()
        #print (book_index)
        content = book.cookie_login(stnumber,passwd)
        return jsonify (content)

@app.route('/new_book',methods=['GET','POST'])
def get_newbook():
    if request.method == 'POST':
        page = request.form.get('page')
        from app import new_book
        newbook = new_book.Main()
        content = newbook.get_newbook(page)
        return jsonify(content)

@app.route('/hot_book',methods=['GET','POST'])
def get_hot_book():
    if request.method == 'POST':
        from app import hot_book
        book = hot_book.Main()
        content = book.get_hotbook()
        return jsonify(content)

@app.route('/notice_list',methods=['GET','POST'])
def get_notice_list():
    if request.method == 'POST':
        from app import notice_list
        page = request.form.get('page')
        book = notice_list.Main()
        content = book.get_notice_list(page)
        return jsonify(content)
		
@app.route('/notice_content',methods=['GET','POST'])
def get_notice_content():
    if request.method == 'POST':
        from app import notice_content
        href = request.form.get('href')
        book = notice_content.Main()
        content = book.get_notice_content(href)
        return jsonify(content)
		
@app.route('/get_data',methods=['GET','POST'])
def get_data():
    if request.method == 'POST':
        from app import data_sourse
        book = data_sourse.Main()
        content = book.get_data()
        return jsonify(content)

		

>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
=======
     app.run (debug=True)
>>>>>>> 0701ef0291a1b1ea8e0b31c609c273778a34a1c0
