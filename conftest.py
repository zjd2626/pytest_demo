import pytest
import xlrd
import smtplib


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     out = yield
#     report = out.get_result()
#     print(out)
#     print(report)
#     print(report.when)
#     print(report.nodeid)
#     print(report.outcome)

# @pytest.fixture(scope='module')
# def smtp_connection_request(request):
#     server, port = getattr(request.module, 'smtp_server', ("smtp.163.com", 25))
#     with smtplib.SMTP(server, port, timeout=5) as smtp_connection:
#         yield smtp_connection
#         print("断开 %s：%d" % (server, port))


@pytest.fixture(scope="session")
def init_driver():
    pass


def gen_data():
    wookbook = xlrd.open_workbook("data/userdata.xls")
    sheet = wookbook.sheet_by_index(0)
    nrows = sheet.nrows
    data = []
    for i in range(1, nrows):
        data.append(sheet.row_values(i))
    return data

@pytest.fixture(scope="session", params=gen_data())
def init_data(request):
    yield request.param
