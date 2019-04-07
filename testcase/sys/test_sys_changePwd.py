import pytest,allure
from conftest import http
from common.CommonData import Commondata
@allure.feature('修改密码')
class Test_changes:
    @pytest.mark.debug
    @allure.story('修改密码')
    def test_changepwd(self):
        path='/sys/changePwd'
        data={
            'token':Commondata.token,
            'userId':157,
            'userName':Commondata.userName,
            'oldPwd':Commondata.password,
            'password':Commondata.newpassword
        }
        resp1=http.post(path, data)
        assert resp1['code']==200
        assert resp1['msg']=='操作成功'
    @pytest.mark.debug
    @allure.story('修改密码后登录')
    def test_relogin(self):
        path='/sys/login'
        data={
            'userName':Commondata.userName,
            'password':Commondata.newpassword
        }
        resp1=http.post(path, data)
        assert resp1['code']==200
        assert resp1['msg']=='操作成功'
