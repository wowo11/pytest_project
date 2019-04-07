from util.httputil import *
from common.CommonData import *
http=HttpUtil()
common=Commondata()
class Test_ll:
    def test_login_failed01(self):
        path='/sys/login'
        data = {'userName':common.userName,'password':'123131'}
        resp1 = http.post(path, data)
        assert resp1['code']==410
        assert resp1['msg']=='用户名或密码错误'

    def test_login_failed02(self):
        path='/sys/login'
        data={'userName':'','password':'123456'}
        resp1 = http.post(path, data)
        assert resp1['code']==200
        assert resp1['msg'] == '操作成功'
        # assert resp1['object']['userId'] == 79
    def test_login_failed03(self):
        path='/sys/login'
        data={'password':'123456'}
        resp1 = http.post(path, data)
        assert resp1['code']==301
        assert resp1['msg']=='用户不存在'
        assert resp1['object']==None
    def test_login_failed04(self):
        path='/sys/login'
        data={'userName':'182100345784564','password':'123456'}
        resp1 = http.post(path, data)
        assert resp1['code']==301
        assert resp1['msg']=='用户不存在'
        assert resp1['object'] == None