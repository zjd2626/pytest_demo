import pytest

@pytest.fixture(scope="module",params=[i for i in range(1,4)])
def repeat(request):
    yield request.param


@pytest.mark.apitest
class TestOrder(object):
    @pytest.mark.smoke
    def test_order_02(self):
        print("test_order.py test_order_02")
        # assert 1==2

    # @pytest.mark.dependency(depends=["testcases/test_cart.py::test_cart_02"],scope="session")
    @pytest.mark.dependency(depends=["cart"], scope="session")
    def test_order_01(self):
        print("test_order.py test_order_01")

    def test_order_03(self,repeat):
        print("test_order.py repeat",repeat)
        if repeat==3:
            if 1==1:
                pytest.xfail("第三次执行预期失败")
                # assert False


if __name__ == '__main__':
    pytest.main(["-s", "test_order.py"])