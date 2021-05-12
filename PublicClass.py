#!__author__ = "yf"
"""
pycharm
"""
import requests
import json

url = "http://passport.ablesky.com:80/login.do"


param = {
    'j_username': 'astest-fy',
    'j_password': 'D93591BDF7860E1E4EE2FCA799911215',
    'src': 'android'
}

headers = {
    'Referer': 'http://www.ablesky.com/index.do',
    'User-Agent': 'AbleClass(ableskyapp)',
    'AS-Agent': 'AbleClass(ableskyapp)',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Connection': 'Keep-Alive'
}
res = requests.get(url= url, params = param, headers=headers, verify = False)
print(res.status_code)
print(res.content)

# res.content为二进制，转换成字符串
strContent = str(res.content, encoding="utf8")
print(strContent)
print(type(strContent))

# str转成json
jsonContent = json.loads(strContent)
print(jsonContent)
print(type(jsonContent))

print(jsonContent.keys())
print(jsonContent.values())

print(jsonContent['id'])
print(jsonContent['success'])
# 校验
assert jsonContent['success'] == True
