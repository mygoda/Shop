# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
"""
raven
"""

import logging
import os

from raven import Client

logger = logging.getLogger("miss")

try:
    sentry_url = 'sentry url'
    client = Client(sentry_url)
except:
    client = None
    logger.warning('settings.sentry.sentry_url is not defined!')


def capture_exception():
    if client:
        client.captureException()


def capture_message(message, **kwargs):
    if client:
        client.captureMessage(message, **kwargs)