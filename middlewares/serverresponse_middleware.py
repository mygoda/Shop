# -*- coding:utf-8 -*-
import logging
import json

from django.http.response import JsonResponse
# from libs.errors import ServerError
# from django.http import HttpResponseRedirect
# from users.models import AccessToken, User
import traceback
from django.conf import settings

# 此处不需要传access token的接口配置
SKIP_PATH = [

]


class ServerResponseMiddleware(object):

    _initial_http_body = None
    user_id = None
    language = None

    def process_request(self, request):
        pass

    def process_exception(self, request, exception):
        return JsonResponse({"status": 0, "msg": str(exception)})
