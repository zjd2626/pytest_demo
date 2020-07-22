import pytest
import requests
import allure
import xlrd

@allure.step("step:浏览商品")
def open_goods():
    '''浏览商品'''
    print("浏览商品")

@allure.step("step:添加购物车")
def add_shopping_cart(goods_id="10086"):
    '''添加购物车'''
    print("添加购物车")

@allure.step("step:生成订单")
def buy_goods():
    '''生成订单'''
    print("buy")

@allure.step("step:支付")
def pay_goods():
    '''支付'''
    print("pay")

@allure.feature("功能模块")
@allure.story("测试用例小模块")
class TestBaidu(object):

    @allure.title("测试用例名称：语言检测")
    def test_fy(self):
        data = {
            "query": "It's a nice day."
        }
        r = requests.post("https://fanyi.baidu.com/langdetect", data=data)
        print(r.json())
        allure.attach(name="响应信息",body=r.text)


    @allure.title("测试用例名称：test_02")
    def test_02(self):
        assert 0

    @allure.title("测试用例名称：test_03")
    def test_03(self):
        assert 0==0



if __name__ == '__main__':
    pytest.main(["-s", "test_baidu.py"])