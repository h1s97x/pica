import hashlib
import hmac
import json
import os
from configparser import ConfigParser
from datetime import datetime
from time import time
from urllib.parse import urlencode

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base = "https://picaapi.picacomic.com/"

class Pica:
    Order = {
        'default': 'ua',  # 默认
        'latest': 'dd',  # 新到旧
        'oldest': 'da',  # 旧到新
        'loved': 'ld',  # 最多爱心
        'point': 'vd'  # 最多指名
    }

    def __init__(self):
        self.api = requests.Session()
        self.token = None

        parser = ConfigParser()
        parser.read('./config.ini', encoding='utf-8')
        self.headers = dict(parser.items('header'))
        
    def http_do(self, method, url, **kwargs):
        kwargs.setdefault("allow_redirects", True)
        header = self.headers.copy()
        ts = str(int(time()))
        raw = url.replace(base, "") + str(ts) + header["nonce"] + method + header["api-key"]
        # print('PICA_SECRET_KEY: ' + os.environ["PICA_SECRET_KEY"], flush=True)
        hc = hmac.new(os.environ["PICA_SECRET_KEY"].encode(), digestmod=hashlib.sha256)
        hc.update(raw.lower().encode())
        header["signature"] = hc.hexdigest()
        header["time"] = ts
        kwargs.setdefault("headers", header)
        proxy = os.environ.get("REQUEST_PROXY")
        if proxy:
            proxies = {'http': proxy, 'https': proxy}
        else:
            proxies = None
        response = self.api.request(method=method, url=url, verify=False, proxies=proxies, **kwargs)
        return response

    def login(self, account, password):
        url = base + "auth/sign-in"
        data = {
            'email': account,
            'password': password
        }
        response = self.http_do("POST", url=url, json=send).text
        print("login response:{}".format(response), flush=True)
        if json.loads(response)["code"] != 200:
            raise Exception('PICA_ACCOUNT/PICA_PASSWORD ERROR')
        if 'token' not in res:
            raise Exception('PICA_SECRET_KEY ERROR')
        self.headers["authorization"] = json.loads(response)["data"]["token"]
        # self.token = response['token']

def main():
    env = os.environ
    PICA_ACCOUNT = env.get('PICA_ACCOUNT')
    PICA_PASSWORD = env.get('PICA_PASSWORD')

    account = PICA_ACCOUNT
    password = PICA_PASSWORD

    pica = Pica()
    pica.login(account, password)



