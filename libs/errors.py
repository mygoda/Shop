# -*- coding:utf-8 -*-
import json

error_dict = {}


class ServerError(Exception):

    def __init__(self, code, *args):
        self.code = code
        self.msg = error_dict[code]

    def __str__(self):
        return json.dumps({"code": self.code, "msg": self.msg, "data": {}})

    def json(self):
        return {"code": self.code, "msg": self.msg, "data": {}}

error_dict[0] = u"没有权限,无法执行该请求"


def throw_exception(logger, error_msg):
    """
        抛出异常 sentry
    :param logger:
    :param error_msg:
    :return:
    """
    logger.info(error_msg)
    logger.error(error_msg)
