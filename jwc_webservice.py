from urllib import parse,request
import json
from flask import Flask, jsonify
from flask import request
import urllib
from bs4 import BeautifulSoup
from app import app
import requests


@app.route('/main_fun', methods=['GET','POST'])
def main_fun():
    if request.method == 'POST':
        dic1 = request.form
        print(dic1.to_dict())
        dic2 = dic1.to_dict()
        dic3 = parse.urlencode (dic2).encode (encoding='utf-8')
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/x-www-form-urlencoded"}
        url = 'http://59.72.194.12:8086/index.aspx'
        req = urllib.request.Request (url=url, data=dic3, headers=header_dict)
        res = urllib.request.urlopen (req)
        final_data = res.read ( ).decode ('utf-8')
        print (final_data)
        return final_data
        #return jsonify(dic1)

@app.route('/table', methods=['GET','POST'])
def get_table():
    if request.method == 'POST':
        username = request.form.get('studentNo')
        pwd = request.form.get('password')
        from app import login_cookies_new
        cookiee = login_cookies_new.main ( )
        cookies = cookiee.get_cookie (username, pwd)
        url2 = 'http://59.72.194.13/TimetableSearch/TimetableSerachStudentSingleSpan.aspx'
        r = requests.get (url2, cookies=cookies)
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
             textx = td.getText('\n')
             listx = textx.split('\n')
             print(listx)
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
        book_name = request.form.get('book_name')
        from app import book_main
        book = book_main.main ( )
        content = book.get_content (book_name)
        list1 = book.get_booklist (content)
        list2 = book.get_booklistdetail (content)
        #list3 = book.get_index (list1)
        list4 = book.get_json (list1, list2)
        print (list4)
        #from spider_book import global_ls
        #global_ls.global_list = list3
        return jsonify (list4)


@app.route('/book_content',methods=['GET','POST'])
def get_book_content():
    if request.method == 'POST':
        book_index = request.form.get('book_index')
        from app import book_main
        book = book_main.main ()
        print (book_index)
        content = book.get_detail (book_index)
        return jsonify (content)



if __name__ == "__main__":

     app.run (debug=True)