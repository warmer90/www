import requests
import yaml


class BaseApi:

    def send_api(self, req):
        """
        1.先把请求信息转为一个json结构体
        2.在bese_api里面对requests.request进行封装
        3.传入为json结构体的请求信息。给requests.request
            使用关键字传参的方式传入  要注意解包  用“**”
        :param req: 一个json结构体
        :return:
        """
        # requests.request()
        return requests.request(**req)
    def load(self,file):
        return yaml.safe_load(open(file))