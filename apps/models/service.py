# -*- coding: utf-8 -*-
# __author__ = xutao

from django.db import models
from common.models import CommonModelMixin
from apps.models import Shop


class Service(CommonModelMixin, models.Model):
    """
        服务
    """

    name = models.CharField(u"服务名称", max_length=32)
    shop = models.ForeignKey(Shop, verbose_name=u"店面", null=True, blank=True)
    is_valid = models.BooleanField(u"是否有效", default=True)

    def __unicode__(self):
        return "%s:%s" % (self.name, self.shop.name)
