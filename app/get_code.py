import requests
from flask import Flask, jsonify
import json

class main(object):
  def get_code(self,code):
      content = {
      'appid': 'wx734236db46cac3ae',
      'secret': '5c62fad4852db8299f363d5497448ad0',
      'js_code': code,
      'grant_type': 'authorization_code'
      }
      r = requests.get('https://api.weixin.qq.com/sns/jscode2session', params = content)
      return r.content