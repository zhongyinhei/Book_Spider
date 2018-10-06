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
       if len(list1[i][0])>15:
           jsonlist['name'] = list1[i][0][0:15]+"..."
       else:
           jsonlist['name'] = list1[i][0]
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
      print(index)
      return index

  def get_detail(self,remove):

    page_url = 'http://202.198.14.5:8080/opac/item.php?marc_no=0000241283'
    remove2 = "item.php?marc_no="+remove
    print(remove2)
    new_full_url = parse.urljoin(page_url,remove2)
    print(new_full_url)
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
    temp3 = json.dumps(tempdic,ensure_ascii=False)
    print(temp3)
    tables = soup.findAll ('table', id='item')
    tab = tables[0]
    cont = tab.findAll ('tr')
    lists = []

    for i in range (1, len (tab.findAll ('tr'))):
        list = []
        for td in cont[i].find_all ('td'):
            text = td.text
            text2 = text.split (' ')
            list.append (text2)
            print(list)
        lists.append (list)
    lists.append(temp3)
    print (lists)
    return  lists



