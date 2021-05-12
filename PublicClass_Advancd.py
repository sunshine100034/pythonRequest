#!__author__ = "yf"
"""
pycharm
"""
import unittest
import requests
import json
# import ddt   报 not callable  class用ddt.ddt修饰
from ddt import ddt, file_data, data
from readYamlData import getYamlData


def ByteToJson(content):
    strContent = str(content, encoding="utf8")
    print(strContent)
    print(type(strContent))

    # str转成json
    jsonContent = json.loads(strContent)
    print(jsonContent)
    print(type(jsonContent))
    return jsonContent

@ddt
class TestPublicClass(unittest.TestCase):

    def setUp(self) -> None:
        print('test start')
        self.headers = {
            'Referer': 'http://www.ablesky.com/index.do',
            'User-Agent': 'AbleClass(ableskyapp)',
            'AS-Agent': 'AbleClass(ableskyapp)',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Connection': 'Keep-Alive'
        }
        self.url = 'http://passport.ablesky.com:80/login.do'

    def tearDown(self) -> None:
        print("test closed")

    @file_data('data.yaml')
    def test_Case1(self, **arg):
        print('test case1 start')
        print(arg)
        res = requests.get(url=self.url, params=arg, headers=self.headers, verify=False)
        jsonContent = ByteToJson(res.content)
        print(res.status_code)
        self.assertEqual(res.status_code, 200, "status code is not 200")
        self.assertTrue(jsonContent['success'], 'success is not true')
        print('test case1 end')
        # requests.get(arg)
        return


    testData = getYamlData()
    @data(*testData)
    def test_Case2(self, arg):
        print('test case2 start')
        print(arg)
        print('test case2 end')
        return


if __name__ == '__main__':
    unittest.main()
