import random,pytest
import allure
from conftest import http
from common.CommonData import Commondata
@allure.feature('注册登录再比较')
class Test_load:
    @pytest.mark.debug
    @allure.story('注册')
    def test_register(self):
        path = '/user/saveOrUpdateUser'
        nickname=str(random.randint(10000000,100000000))
        username='155'+nickname
        print(username)
        data={"nickName":nickname,
              "userName": username,
              "telNo":"","email":"","address":"",
              "roleIds":"1","regionId":1,"regionLevel":1}
        resp1=http.post(path, data)
        print('注册成功')

        path2='/sys/login'
        login_data = {'userName':username,'password':Commondata.password}
        resp2=http.post(path2,login_data)
        print('登录成功')
        print(resp2)
        id1 = resp2['object']['userId']
        id2 = self.getId()
        assert id1 == id2
    @pytest.mark.debug
    @allure.story('获取id')
    def getId(self):
        path3= '/user/loadUserList'
        data = {"pageCurrent":1,"pageSize":10}
        resp= http.post(path3, data)
        r = resp['object']['list'][0]['id']
        return r