import json
import time
from optparse import Option

import requests

from phoenix.option import Option
from phoenix.struct import Param, UserInfo, recommendReq
from phoenix.util import rand_str, cal_signature


class Client:
    def __init__(self, param: Param):
        self._param = param

    def write_data(self, topic: str, stage: str, param: list, *opts: Option):
        url = f"{self._param.write_url}{self._param.project_id}/{topic}/{stage}"
        param = json.dumps(param).replace(" ", "")
        return self.api_request(url, Option.conv_to_options(opts).request_id, param)

    def rec(self, scene: int, user: UserInfo, *opts: Option):
        url = f"{self._param.rec_url}{self._param.project_id}"
        req = recommendReq(
            self._param.customer_id,
            self._param.project_id,
            scene,
            user.__dict__,
        )
        param = json.dumps(req.__dict__).replace(" ", "")
        return self.api_request(url, Option.conv_to_options(opts).request_id, param)

    def api_request(self, url: str, request_id: str, param):
        time_now = str(int(time.time()))
        nonce = rand_str(8)
        if not request_id:
            request_id = rand_str(16)
        signature = cal_signature(
            str(self._param.customer_id),
            time_now,
            self._param.ak,
            self._param.sk,
            nonce,
            param,
        )
        headers = {
            "content-type": "application/json",
            "Customer-Id": str(self._param.customer_id),
            "Access-Id": self._param.ak,
            "Time": time_now,
            "Nonce": nonce,
            "Request-Id": request_id,
            "Signature": signature,
        }
        return requests.post(url, data=param, headers=headers).json()
