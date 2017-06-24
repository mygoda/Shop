# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
import imghdr

from qiniu import put_data, Auth, put_file
import requests
from django.conf import settings

q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
q_token = q.upload_token(bucket=settings.BUCKET_NAME, expires=31536000)

def get_qiniu_token():
    """
        获取 七牛 token
    :return:
    """
    qiniu = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
    qiniu_token = qiniu.upload_token(bucket=settings.BUCKET_NAME, expires=31536000)
    return qiniu_token


def detect_image_type(content):
    return imghdr.what("", h=content)


def upload_img_by_url(url, filename):
    r = requests.get(url=url, stream=True)
    return upload_img(stream=r.content, filename=filename)


def upload_img(stream, filename):
    put_data(up_token=q_token, key=filename, data=stream)
    return '%s/%s' % (settings.IMAGE_URL_PRE, filename)

