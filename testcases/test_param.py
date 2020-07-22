import pytest

seq=["case1","case2","case3"]


@pytest.fixture(scope="module",params=seq)
def params(request):
    return request.param


def test_params(params):
    print(params)
    assert "case" in params


if __name__ == '__main__':
    pytest.main(["-s","test_param.py"])