# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django import template
from django.conf import settings

import json

register = template.Library()


@register.inclusion_tag('widgets/g_user.html')
def g_user_script(request):
    user = request.user
    if not user.is_authenticated():
        context = {
            "g_user_id": "",
            "g_user_username": "",
            "g_user_phone": ""
        }
    else:
        context = {
            "g_user_id": user.id,
            "g_user_username": user.username,
            "g_user_phone": user.phone
        }
    return context


@register.simple_tag
def static_root(project_name=""):
    debug = settings.CDN_DEBUG
    version_json = settings.STATIC_VERSION_JSON
    if debug:
        env = "dev"
    else:
        env = "pro"
    root = version_json.get(project_name, {}).get(env, {}).get("_root", "")
    return root