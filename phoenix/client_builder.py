from phoenix.client import Client
from phoenix.struct import Param, defaultRecUrl, defaultWriteUrl


class ClientBuilder(object):
    def __init__(self):
        self._param = Param()

    def customer_id(self, customer_id: int):
        self._param.customer_id = customer_id
        return self

    def project_id(self, project_id: int):
        self._param.project_id = project_id
        return self

    def ak(self, ak: str):
        self._param.ak = ak
        return self

    def sk(self, sk: str):
        self._param.sk = sk
        return self

    def rec_url(self, rec_url: str):
        if not rec_url:
            rec_url = defaultRecUrl
        self._param.rec_url = rec_url
        return self

    def write_url(self, write_url: str):
        if not write_url:
            write_url = defaultWriteUrl
        self._param.write_url = write_url
        return self

    def build(self) -> Client:
        return Client(self._param)
