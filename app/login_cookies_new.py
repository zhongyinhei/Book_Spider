#from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import requests

from app import app

class main(object):
    def get_cookie(self,username, pwd):
       Code_url='http://59.72.194.13/VerifyCode.aspx'
       post_url='http://59.72.194.13/login.aspx'
       headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

       session=requests.session()

       session.get(Code_url,headers=headers)
       image_code=session.cookies.get_dict()['CheckCode']

       form_data = {
          '__LASTFOCUS':"",
          '__EVENTTARGET':"",
          '__EVENTARGUMENT':"",
          '__VIEWSTATE':'/wEPDwULLTEyOTMxOTM5ODQPZBYCAgMPZBYSAgMPDxYCHgRUZXh0BRgyMDE3LjEyLjE5IFR1ZXNkYXkgMTk6MzJkZAIHDxYCHwAFEuS4nOWMl+eUteWKm+Wkp+WtpmQCCQ8UKwAFDxYGHgVWYWx1ZQUkNzYzNTkyZTYtMGU2Yy00ZWUwLTkyMTktNWQwYmE3YjljNmIyHg9EYXRhU291cmNlQm91bmRnHg5fIVVzZVZpZXdTdGF0ZWdkZGQ8KwAIAQcUKwADFgYeClZhbHVlRmllbGQFCFBXUm9sZUlEHglUZXh0RmllbGQFCFJvbGVOYW1lHhJFbmFibGVDYWxsYmFja01vZGVoZA8WAh4KSXNTYXZlZEFsbGcPFCsABxQrAAEWCB8ABQbmlZnluIgfAQUkNzYzNTkyZTYtMGU2Yy00ZWUwLTkyMTktNWQwYmE3YjljNmIyHghJbWFnZVVybGUeDlJ1bnRpbWVDcmVhdGVkZxQrAAEWCB8ABQblrabnlJ8fAQUkYmRmZWI4NmUtM2MyOS00Njk2LWExOWQtNmM0Mjg4NTBjZWEzHwhlHwlnFCsAARYIHwAFDOaVmeWtpuenmOS5ph8BBSRlNmM5YmQxMS0wODUzLTQ4YWItYjc0OC1jODE0MDA0YjU5MmEfCGUfCWcUKwABFggfAAUM5pWZ5a2m5bmy5LqLHwEFJDE3MjcxNTRlLTQ1ZjEtNDQ4Ni05OTE0LWVhMDQ4NDc4N2Y0MB8IZR8JZxQrAAEWCB8ABQnnrqHnkIbogIUfAQUkNzAxZjczYmItNTZjNS00ZDIyLWE4YzAtMzU2ODk2NGQ2NDFjHwhlHwlnFCsAARYIHwAFCei+heWvvOWRmB8BBSRhY2MxZmEyNC0wNGM5LTQ0NGItOWY3NS0wMGQ2NDQyZWE3YWMfCGUfCWcUKwABFggfAAUJ5a6e6aqM5a6kHwEFJGZmOTYxZTUzLTU4MTMtNDAwMS1hMmM5LTU1NGQxYjc0ZTA4OB8IZR8JZ2RkFgJmD2QWAgIBDzwrAAgBAA8WBB8CZx8DZ2RkAhUPFCsABA8WBB8BBRxodHRwOi8vd3d3Lmxpbmd6aGFuc29mdC5jb20vHwNnZGRkPCsABAEAFgIfAAUk6ZW/5pil5YeM5bGV6L2v5Lu25pyJ6ZmQ6LSj5Lu75YWs5Y+4ZAIXDxYCHwAFIuWQieael+ecgemVv+aYpeW4guWNq+aYn+i3rzcwODnlj7dkAhkPFgIfAAUGMTMwMDIyZAIbDxYCHwAFFueUteivne+8mjA0MzEtODUzNjE4ODZkAh0PFgIfAGVkAh8PD2QWAh4Fc3R5bGUFDmRpc3BsYXk6YmxvY2s7FgICAQ88KwAWAwAPFggfAmcfA2ceEUNsaWVudFN0YXRlTG9hZGVkZx4NQ2FsbGJhY2tTdGF0ZWRkBg9kEBYBZhYBPCsACwEAFgIeD0NvbFZpc2libGVJbmRleGYPFgECARYBBZcBRGV2RXhwcmVzcy5XZWIuQVNQeEdyaWRWaWV3LkdyaWRWaWV3RGF0YVRleHRDb2x1bW4sIERldkV4cHJlc3MuV2ViLkFTUHhHcmlkVmlldy52OC4zLCBWZXJzaW9uPTguMy40LjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49NTM3N2M4ZTNiNzJiNDA3MwkUKwABFgIeEVNob3dDb2x1bW5IZWFkZXJzaBYCAgEPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgIFCkRYRGF0YVJvdzAPZBYCBQl0Y2NlbGwwXzAPZBYCBQdjZWxsMF8wD2QWAgIBDw8WBB8ABT/lhbPkuo7mlZnliqHns7vnu5/kvb/nlKjliY3nmoTmtY/op4jlmajorr7nva7or7TmmI4oMTIgMjUgMjAxMykeC05hdmlnYXRlVXJsBUlTeXN0ZW1Ub29sL1NUTmV3c0RldGFpbHNTaG93LmFzcHg/SWQ9ZTE0NTYyZTEtNDQ5Ny00YzViLThiYzItMDYwYTU3YzM4M2QxZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFC2NvYlJvbGUkREREBQdncmlkTmV3qBVKhs4aVK8uMmv9GKotlpRYHK3PBOjYDu5H/O41Pnk=',
          '__EVENTVALIDATION':'/wEWCALWnIjKCALLrZqPCAKqydOsDAKjp/vdAQLzpqn0DwLs9tTtBQKM54rGBgLXk6LaBjTaWpMTtnxggm9qU3Md++fsbZPyofgz9xlypxHVXXMq',
          'cobRole_VI': 'bdfeb86e-3c29-4696-a19d-6c428850cea3',
          'cobRole':'学生',
          'cobRole_DDDWS':'0:0:-1:0:0:0:0:0:',
          'cobRole_DDD_LDeletedItems':'',
          'cobRole_DDD_LInsertedItems':'',
          'cobRole_DDD_LCustomCallback':'',
          'cobRole$DDD$L':'bdfeb86e-3c29-4696-a19d-6c428850cea3',
          'cobRole$DDD$L$CVS':'',
          'cobRole$CVS':'',
          'User_ID': username,
          'User_Pass': pwd,
          'txtVolidate': image_code,
          'Button1':'',
          'gridNew$DXSelInput':'',
          'gridNew$CallbackState':'/wEWBB4ERGF0YQWQA0FBQUFBQUVBQUFBQUFBQUFBUUFBQUFBREFBQUFDRk5VVG1WM2MwbEVDRk5VVG1WM2MwbEVDd0FBQlVselRtVjNCVWx6VG1WM0NnQUFET21BbXVlZnBlUy9vZWFCcnd6cGdKcm5uNlhrdjZIbWdhOEhBQUFMQUFBQUNVNWxkM05VYVhSc1pRdE9aWGR6UTI5dWRHVnVkQWxKYzNOMVpVUmhkR1VKU1hOemRXVkVaWEIwQ0ZCWFZYTmxja2xFQmxKbGJXRnlhdzFKYzBSbFptRjFiSFJFYVhOd0NVNWxkM05UWTI5d1pRaE9aWGR6UzJsdVpBZFNaV0ZrVG5WdENrMXZaR2xtZVVSaGRHVUhBQWNBQndBSEFBYi8vd3NDNFdKRjRaZEVXMHlMd2dZS1Y4T0QwUW9DQVFjQ1ArV0ZzK1M2anVhVm1lV0tvZWV6dStlN24rUzl2K2VVcU9XSmplZWFoT2ExaitpbmlPV1pxT2l1dnVlOXJ1aXZ0T2FZamlneE1pQXlOU0F5TURFektRPT0eBVN0YXRlBURCd0VIQUFJQkJ3QUhBQWNBQndBQ0FBYi8vd2tDQ0ZOVVRtVjNjMGxFQ1FJQUFnQURCd1FDQUFjQUFnRUhBQUlCQndBPQ=='
          }
       session.post (post_url, headers=headers, data=form_data)
       cookies = requests.utils.dict_from_cookiejar (session.cookies)
       return cookies
