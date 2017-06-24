# -*- coding: utf-8 -*-
# __author__ = xutao

from django.db import models
from common.models import CommonModelMixin


class Company(CommonModelMixin, models.Model):
    """
        公司
    """

    name = models.CharField(u"公司名称", max_length=255)
    is_valid = models.BooleanField(u"是否有效", default=True)

    def __unicode__(self):
        return self.name


class Shop(CommonModelMixin, models.Model):
    """
        店面
    """

    name = models.CharField(u"店面名称", max_length=255)
    company = models.ForeignKey(Company, verbose_name=u"公司", null=True, blank=True)
    address = models.CharField(u"地址", max_length=255, null=True, blank=True)
    is_valid = models.BooleanField(u"是否有效", default=True)

    def __unicode__(self):
        return self.name


class ShopIndexPic(models.Model):
    """
        店面首页轮播图    
    """

    name = models.CharField(u"描述", max_length=32, null=True, blank=True)
    href = models.CharField(u"链接", max_length=255, null=True, blank=True)
    img = models.CharField(u"图片链接", max_length=255, null=True, blank=True)
    pri = models.IntegerField(u"优先级", default=0, help_text=u"从小到大排列")

    def __unicode__(self):
        return self.name




