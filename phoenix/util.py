import hashlib
import random
import string


def rand_str(length: int):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def cal_signature(
    customer_id: str,
    time_now: str,
    access_id: str,
    access_key_secret: str,
    nonce: str,
    http_body: str,
):
    sha256 = hashlib.sha256()
    sha256.update(
        (
            customer_id + access_id + access_key_secret + time_now + nonce + http_body
        ).encode("utf-8")
    )
    return sha256.hexdigest()
