# -*- coding: utf-8 -*-
# __author__ = xutao
from __future__ import division, unicode_literals, print_function
import json
import requests
from django.conf import settings
# 邮件相关的操作

EMAIL_HOST = settings.EMAIL_HOST
EMAIL_PORT = settings.EMAIL_PORT


def email_api(to, subjects, content):
    """
        发送邮件接口
    """
    url = "http://%s:%s/mail/send/" % (EMAIL_HOST, EMAIL_PORT)

    email_body = {
        "to": to,
        "subjects": subjects,
        "content": content,
    }

    response = requests.post(url, data=json.dumps(email_body))

    if response.ok:
        # 发送成功的情况
        result = response.json()
        data = result.get("data")
        return True, data.get("task_id")
    else:
        return False, response.content


def send_email(to, content, subjects):
    """
        发送邮件
    """
    is_ok, msg = email_api(to=to, subjects=subjects, content=content)
    return is_ok, msg