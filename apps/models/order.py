# -*- coding: utf-8 -*-
# __author__ = xutao

from django.db import models
from common.models import CommonModelMixin
from users.models import Customer
from apps.models import Shop, Service, ServiceStaff


class Order(CommonModelMixin, models.Model):
    """
        订单
    """

    service = models.ForeignKey(Service, verbose_name=u"服务")
    shop = models.ForeignKey(Shop, verbose_name=u"店面")
    staff = models.ForeignKey(ServiceStaff, verbose_name=u"服务人员", null=True, blank=True)
    customer = models.ForeignKey(Customer, verbose_name=u"预订客户")
    order_date = models.DateTimeField(u"预约时间", null=True, blank=True)

    def __unicode__(self):
        return "service:%s, customer:%s" % (self.service.name, self.customer.name)

