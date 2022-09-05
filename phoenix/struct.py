defaultRecUrl = "http://phoenix-api.icocofun.com/recommend/openapi/rec/"
defaultWriteUrl = "http://phoenix-api.icocofun.com/data/openapi/write/"


class Param(object):
    def __init__(self):
        self.project_id: int = 0
        self.customer_id: int = 0
        self.ak: str = ""
        self.sk: str = ""
        self.rec_url: str = ""
        self.write_url: str = ""


class UserInfo(object):
    def __init__(self, user_id, did, ip, channel, network, os, model):
        self.user_id: str = user_id
        self.did: str = did
        self.ip: str = ip
        self.channel: str = channel
        self.network: int = network
        self.os: str = os
        self.model: str = model


class recommendReq:
    def __init__(self, custom_id, project_id, scene_id, user):
        self.custom_id: int = custom_id
        self.project_id: int = project_id
        self.scene_id: int = scene_id
        self.user: UserInfo = user
