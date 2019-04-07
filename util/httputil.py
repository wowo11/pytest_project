import requests,json
from common.CommonData import *
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}
    def post(self,path,data):
        host=Commondata.host
        proxies=Commondata.proxies
        if Commondata.token is not None:
            self.headers['token']=Commondata.token
        data_json=json.dumps(data)
        resp_login=self.http.post(url=host+path,
                       proxies=proxies,
                       data=data_json,
                       headers=self.headers)
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)
        print(resp_dict)
        # assert resp_dict['code'] == 200
        return resp_dict
