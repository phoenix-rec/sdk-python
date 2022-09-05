import unittest
import uuid

from phoenix.client_builder import *
from phoenix.option import Option
from phoenix.struct import UserInfo


class MyTestCase(unittest.TestCase):
    def test_write(self):
        customer_id = 1
        project_id = 10000001
        ak = "accessId"
        sk = "secretId"
        write_url = "http://phoenix-api.icocofun.com/data/openapi/write/"

        client: Client = (
            ClientBuilder()
            .write_url(write_url)
            .customer_id(customer_id)
            .ak(ak)
            .sk(sk)
            .project_id(project_id)
            .build()
        )

        param = [{"x_item_id": "21", "x_status": 1}, {"x_item_id": "6", "x_status": 1}]

        resp = client.write_data(
            "item", "test", param, Option.with_request_id("123456789")
        )
        print(resp)
        return resp['ret'] == 0

    def test_rec(self):
        customer_id = 1
        project_id = 10000001
        ak = "accessId"
        sk = "secretId"
        rec_url = "http://phoenix-api.icocofun.com/data/openapi/rec/"

        client: Client = (
            ClientBuilder()
            .rec_url(rec_url)
            .customer_id(customer_id)
            .ak(ak)
            .sk(sk)
            .project_id(project_id)
            .build()
        )

        userId = "13065"
        did = "asdfghjkl"
        ip = "127.0.0.1"
        channel = "HuaiWei"
        network = 1
        os = "Android"
        model = "HUAWEI P40"
        user = UserInfo(userId, did, ip, channel, network, os, model)

        resp = client.rec(10001, user, Option.with_request_id(str(uuid.uuid1())))
        print(resp)
        return resp['ret'] == 0


if __name__ == "__main__":
    unittest.main()
