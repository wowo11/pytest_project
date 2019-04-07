import pytest
from util.httputil import *
http =HttpUtil()
from common.CommonData import *
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path='/sys/login'
    data={
        'userName':Commondata.userName,
        'password':Commondata.password
    }
    resp1=http.post(path,data)
    Commondata.token=resp1['object']['token']
