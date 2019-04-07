# import pytest,requests,json
# @pytest.fixture(scope='function',autouse=True)
# def test_myexamp():
#     proxies = {'http': 'http://localhost:8888'}
#     headers = {}
#     headers['Content-Type'] = 'application/json;charset=UTF-8'
#     http = requests.session()
#     resp = http.post(url='http://192.168.1.203:8083/sys/login', proxies=proxies,
#                      data='{"userName":"18210034706","password":"123456"}',
#                      headers=headers)
#     assert resp.status_code == 200
#     print(resp.status_code, '........................')
#     yield
#     resp_dict = json.loads(resp.text)
#     token = resp_dict['object']['token']  # 获取token值
#     headers['token'] = token  # token值添加到字典中
#     data_token = {'token': token}
#     resp = http.post(url='http://192.168.1.203:8083/sys/logout', proxies=proxies,
#                      data=data_token,headers=headers)
#     assert resp.status_code==200