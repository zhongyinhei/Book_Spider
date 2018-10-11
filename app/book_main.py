from bs4 import BeautifulSoup
from urllib import request
import urllib
import string
import re
from urllib import parse
from urllib.request import urlopen
import json

from app import app

class main(object):
  def get_json(self,list1,list2):
      listn = []
      for i in range (0, len (list1)):
       jsonlist = {}
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
       if len(list1[i][0])>15:
           jsonlist['name'] = list1[i][0][0:15]+"..."
       else:
           jsonlist['name'] = list1[i][0]
<<<<<<< HEAD
=======
=======
       jsonlist['name'] = list1[i][0]
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
       jsonlist['idd'] = list1[i][1]
       jsonlist['sum'] = list2[i][0]
       jsonlist['avi'] = list2[i][1]
       jsonlist['pub_year'] = list2[i][2]
       listn.append(jsonlist)
      #print(listn)
      return listn
  def get_content(self,book):
      full_url = 'http://202.198.14.5:8080/opac/openlink.php?historyCount=1&strText=c语言&doctype=ALL&strSearchType=title&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL'
      # book = input()
      half_url = "openlink.php?historyCount=1&strText=" + book + "&doctype=ALL&strSearchType=title&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL"
      url = parse.urljoin (full_url, half_url)
      link = urllib.parse.quote (url, safe=string.printable)
      response = request.urlopen (link)
      content = response.read ( )
      soup = BeautifulSoup (content, 'html.parser', from_encoding='utf-8')
      return soup
<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
      
  def get_numpage(self,book,pagenum):
      full_url = 'http://202.198.14.5:8080/opac/openlink.php?historyCount=1&strText=c语言&doctype=ALL&strSearchType=title&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL'
      # book = input()
      half_url = "openlink.php?historyCount=1&strText=" + book + "&doctype=ALL&strSearchType=title&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL&page="+pagenum
      url = parse.urljoin (full_url, half_url)
      link = urllib.parse.quote (url, safe=string.printable)
      response = request.urlopen (link)
      content = response.read ( )
      soup = BeautifulSoup (content, 'html.parser', from_encoding='utf-8')
      return soup
      
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
  def get_booklist(self, soup):
    content2 = soup.find_all ('h3')
    list4 = []
    for i in range(0,len(content2)):
        list3 = []
        value = content2[i].find('a').text
        value2 = content2[i].find('a')
        key = value2['href']
        list3.append(value)
        list3.append(key)
        list4.append(list3)
    return list4

  def get_booklistdetail(self,soup):
    content3 = soup.find('ol', id= 'search_book_list')

    lists = []
    for i in range(0,len(content3)):
        list = []
        if i%2==1:
            a2 = (content3.contents[i].find ('p'))
            b2 = a2.text
            c3 = b2.split (' ')
            list.append (c3[1])
            list.append (c3[44])
            list.append (c3[len (c3)-4])
            lists.append (list)
        else:
         continue
    return lists


  def get_index(self,list4):
      index = []
      for i in range(len(list4)):
          index.append (list4[i][1])
<<<<<<< HEAD
      print(index)
=======
<<<<<<< HEAD
      print(index)
=======
      #print(index)
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
      return index

  def get_detail(self,remove):

    page_url = 'http://202.198.14.5:8080/opac/item.php?marc_no=0000241283'
    remove2 = "item.php?marc_no="+remove
<<<<<<< HEAD
    print(remove2)
    new_full_url = parse.urljoin(page_url,remove2)
    print(new_full_url)
=======
<<<<<<< HEAD
    print(remove2)
    new_full_url = parse.urljoin(page_url,remove2)
    print(new_full_url)
=======
    #print(remove2)
    new_full_url = parse.urljoin(page_url,remove2)
    #print(new_full_url)
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
    response = request.urlopen(new_full_url)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    content5 = soup.find('div', id= 'item_detail')
    tempdic = {}
    for i in range(0,len(content5)):
     if content5.contents[i].find('dd') == -1 or content5.contents[i].find('dd') == None:
            continue
     else:
            temp = (content5.contents[i].find ('dt'))
            temp2 = (content5.contents[i].find ('dd'))
            tempdic[temp.get_text()] = temp2.get_text()
<<<<<<< HEAD
    temp3 = json.dumps(tempdic,ensure_ascii=False)
    print(temp3)
=======
<<<<<<< HEAD
    temp3 = json.dumps(tempdic,ensure_ascii=False)
    print(temp3)
=======
    #temp3 = json.dumps(tempdic,ensure_ascii=False)
    #print(temp3)
    #print(tempdic)
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据
    tables = soup.findAll ('table', id='item')
    tab = tables[0]
    cont = tab.findAll ('tr')
    lists = []

    for i in range (1, len (tab.findAll ('tr'))):
        list = []
        for td in cont[i].find_all ('td'):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 增加爬取图书馆通知数据
            text = td.text
            text2 = text.split (' ')
            list.append (text2)
            print(list)
        lists.append (list)
    lists.append(temp3)
    print (lists)
    return  lists
<<<<<<< HEAD
=======
=======
           text = td.text
           text2 = text.split (' ')
           list.append (text2)
           #print(list)
        dic_book = {}
        dic_book["ss_num"] = list[0][0]
        dic_book["tm_mun"] = list[1][0]
        dic_book["date"] = list[2][0]
        dic_book["location"] = list[3][12]
        #print (list[3][12])
        dic_book["state"] = list[4][0]
        lists.append (dic_book)
    #lists.append(temp3)
    #print (lists)
    return_list = []
    return_list.append(lists)
    return_list.append(tempdic)
    #print(return_list)
    #return tempdic
    return  return_list
>>>>>>> 2018,10,11(增加爬取图书馆通知数据)
>>>>>>> 增加爬取图书馆通知数据


