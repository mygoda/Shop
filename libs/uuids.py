# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function

import uuid
import random
import hashlib


def create_uuid(name=""):
    """
        创建 uuid
    """
    return str(uuid.uuid4())


def get_uuid():
    u = uuid.uuid4()
    return str(u).replace("-", "")


def create_sms_code():
    codes = ""
    for i in range(4):
        code = random.randrange(10)
        codes += str(code)
    return codes


def md5(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()


