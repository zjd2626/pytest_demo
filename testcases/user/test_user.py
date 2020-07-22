import allure
import pytest


# @pytest.mark.parametrize(['username', 'password'], [('jack', "engine"), ('david', "123456")])
# def test_login(username, password):
#     info = {
#         "jack": "e8dc4081b13434b45189a720b77b6818",
#         "david": "1702a132e769a623c1adb78353fc9503"
#     }
#     import hashlib
#     assert hashlib.md5(password.encode()).hexdigest() == info[username]


# @pytest.mark.usefixtures("init_data")
def test_login_excel(init_data):
    print("login with username: {} ,password: {}.".format(init_data[0],init_data[1]))
    allure.attach(name="传参",body="login with username: {} ,password: {}.".format(init_data[0],init_data[1]))


if __name__ == '__main__':
    pytest.main(["-s", "test_order.py"])
