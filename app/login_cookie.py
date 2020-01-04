from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

from app import app

class main(object):
    def get_cookie(self,username, pwd):
        url_login = 'http://jwc.neepu.edu.cn/'
        driver = webdriver.PhantomJS ( )
        driver.get (url_login)
        # username = '2016302030133'
        # passw = '2016302030133'
        Select (driver.find_element_by_name (
            'ctl00$ctl00$ContentPlaceHolder1$RightContent$ddlIdentity')).select_by_visible_text ('学生')
        user = driver.find_element_by_id ('ctl00_ctl00_ContentPlaceHolder1_RightContent_tbUid')
        user.send_keys (username)
        password = driver.find_element_by_id ('ctl00_ctl00_ContentPlaceHolder1_RightContent_tbPwd')
        password.send_keys (pwd)
        button = driver.find_element_by_id ('ctl00_ctl00_ContentPlaceHolder1_RightContent_imgbtnSubmit')
        button.click ( )
        time.sleep (5)
        cookie = "; ".join ([item["name"] + "=" + item["value"] + "\n" for item in driver.get_cookies ( )])
        # print(cookie)
        # driver.get("http://59.72.194.13/TimetableSearch/TimetableSerachStudentSingleSpan.aspx")
        # m = driver.find_element_by_xpath("//form[@id = 'form1']")
        # print(m)
        cookies = {}
        for line in cookie.split (';'):  # 其设置为1就会把字符串拆分成2份
            name, value = line.strip ( ).split ('=', 1)
            cookies[name] = value
        return cookies