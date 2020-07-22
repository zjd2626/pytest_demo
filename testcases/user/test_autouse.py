import pytest
import time


def test_1(timer_session_scope):
    print("timer_session_scope",timer_session_scope)
    time.sleep(1)

def test_2(timer_session_scope):
    print("timer_session_scope",timer_session_scope)
    time.sleep(2)


if __name__ == '__main__':
    pytest.main(["-s", "test_autouse.py"])