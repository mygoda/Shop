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
    desc = models.CharField(u"描述", max_length=255, null=True, blank=True)
    is_valid = models.BooleanField(u"是否有效", default=True)

    def __unicode__(self):
        return "%s:%s" % (self.name, self.shop.name)

    @property
    def service_imgs(self):
        """
            服务照片
        :return: 
        """
        return self.serviceimage_set.all()

    @property
    def service_items(self):
        return self.serviceitem_set.all()

    @property
    def service_staff(self):
        return self.servicestaff_set.all()


class ServiceImage(models.Model):
    """
        服务图片
    """

    name = models.CharField(u"服务名称", max_length=32, null=True, blank=True)
    service = models.ForeignKey(Service, verbose_name=u"服务", null=True, blank=True)
    url = models.CharField(u"图片地址", max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name


class ServiceItem(models.Model):

    name = models.CharField(u"项目名称", max_length=32)
    desc = models.CharField(u"项目描述", max_length=64)
    service = models.ForeignKey(Service, verbose_name=u"商店", null=True, blank=True)

    def __unicode__(self):
        return "%s:%s" % (self.name, self.desc)


class ServiceStaff(models.Model):
    """
        服务人员
    """

    name = models.CharField(u"理发师名称", max_length=32)
    service = models.ForeignKey(Service, verbose_name=u"服务")
    shop = models.ForeignKey(Shop, verbose_name=u"店面", null=True, blank=True)
    img = models.CharField(u"头像", max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s:%s" % (self.shop.name, self.name)

    @property
    def staff_tags(self):
        return self.stafftag_set.all()


class StaffTag(models.Model):

    staff = models.ForeignKey(ServiceStaff, verbose_name=u"服务人员")
    tag = models.CharField(u"标签名称", max_length=32, null=True)

    def __unicode__(self):
        return "%s:%s" % (self.staff.name, self.tag)

