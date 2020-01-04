import io
import pytesseract
from PIL import Image
import random
import requests
from flask import jsonify


class main(object):

    def cookie_login(self, number, passwd):
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
        mainurl = "http://202.198.14.5:8080/reader/redr_verify.php"
        randomnum = random.uniform (0, 1)
        checkcode_url = 'http://202.198.14.5:8080/reader/captcha.php?' + str (randomnum)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        }
        session = requests.session()
        code_pic = session.get (checkcode_url, headers=headers)
        image = Image.open(io.BytesIO (code_pic.content))
        imgry = image.convert('L')
        threshold = 140
        table = []
        for i in range (256):
            if i < threshold:
                table.append (0)
            else:
                table.append (1)
        out = imgry.point (table, '1')
        vcode = pytesseract.image_to_string (out)
        form_data = {
            'number': number,
            'passwd': passwd,
            'captcha': vcode,
            'select': 'cert_no',
            'returnUrl': ''
        }
        session.post (mainurl, headers=headers, data=form_data)
        cookies = requests.utils.dict_from_cookiejar (session.cookies)
        form_data2 = {
            'para_string': 'all'
        }
        infourl = 'http://202.198.14.5:8080/reader/book_hist.php'
        r2 = requests.post (infourl, cookies=cookies, data=form_data2)
        try:
         from bs4 import BeautifulSoup
         soup = BeautifulSoup(r2.content, 'html.parser', from_encoding='utf-8')
         tables = soup.find('table')
         tr = tables.findAll('tr')
         listsum = []
         for i in range(1, len(tr)):
                listx = []
                dic = {}
                for j in tr[i].findAll ('td'):
                    listx.append (j.text)
                dic['num'] = listx[0]
                dic['book_num'] = listx[1]
                dic['book_name'] = listx[2]
                dic['author'] = listx[3]
                dic['start_t'] = listx[4]
                dic['over_t'] = listx[5]
                dic['loc'] = listx[6]
                listsum.append (dic)
         return listsum
        except:
            return "erro"
