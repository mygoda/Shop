# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function

import urllib

from django.http import HttpResponse
import json
import urlparse

from django.http import JsonResponse


def json_forbidden_response(json_data, msg="", info="", **kwargs):
    data = json_data
    common_response_data = {
        "status": 403,
        "msg": msg,
        "info": info,
        "data": data,
    }
    return HttpResponse(json.dumps(common_response_data), content_type='application/json', **kwargs)


def json_success_response(json_data, **kwargs):
    data = json_data
    common_response_data = {
        "status": 200,
        "msg": "ok",
        "info": "",
        "data": data,
    }
    return HttpResponse(json.dumps(common_response_data), content_type='application/json', **kwargs)


def json_404_response(json_data, msg="", info="", status=404, **kwargs):
    data = json_data
    common_response_data = {
        "status": status,
        "msg": msg,
        "info": info,
        "data": data,
    }
    return HttpResponse(json.dumps(common_response_data), content_type='application/json', **kwargs)


def json_error_response(json_data, msg="", info="", status=500, **kwargs):
    data = json_data
    common_response_data = {
        "status": status,
        "msg": msg,
        "info": info,
        "data": data,
    }
    return HttpResponse(json.dumps(common_response_data), content_type='application/json', **kwargs)


def update_url(url, **kwargs):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(kwargs)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)


class ServerJsonResponse(JsonResponse):

    def __init__(self, data):

        response_data = {
            "status": 200,
            "msg": "",
            "info": "",
            "data": data
        }
        super(ServerJsonResponse, self).__init__(response_data)


def req_is_ok(response):
    """
        请求是否成功
    """
    if response.ok:
        res_json = response.json()
        if int(res_json.get("status")) == 500:
            return False
        else:
            return True
    else:
        return False