import pytest

@pytest.mark.apitest
class TestCart(object):
    @pytest.mark.dependency(name='cart')
    @pytest.mark.run(order=2)
    def test_cart_02(self):
        print("test_cart.py test_cart_02")
        assert 1==2

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_cart_01(self):
        print("test_cart.py test_cart_01")

    @pytest.mark.run(order=3)
    def test_cart_03(self):
        print("test_cart.py test_cart_03")