import pytest
import time
import random

@pytest.fixture()
def postcode():
    return '010'

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

@pytest.fixture(scope='session', autouse=True)
def timer_session_scope():
    num = random.randint(1,100)
    print(num)
    start = time.time()
    print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))
    yield num

    finished = time.time()
    print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print('Total time cost: {:.3f}s'.format(finished - start))



@pytest.fixture(scope='function', autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))
