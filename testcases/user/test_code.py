import pytest

def test_postcode(postcode):
    assert postcode == '010'


if __name__ == '__main__':
    pytest.main(["-s", "test_code.py"])