# -*- coding: utf-8 -*-
# __author__ = xutao

from rest_framework import serializers
from apps.models import Shop, Service, ShopIndexPic, ServiceImage, ServiceItem, ServiceStaff, StaffTag


class StaffTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = StaffTag
        fields = ("id", "tag")


class ServiceImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ServiceImage
        fields = "__all__"


class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = "__all__"


class ShopServiceListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"


class ServiceItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = ServiceItem
        fields = "__all__"


class ServiceStaffSerializers(serializers.ModelSerializer):

    staff_tags = StaffTagSerializers(many=True)

    class Meta:
        model = ServiceStaff
        fields = ("id", "name", "img", "staff_tags")


class ShopServiceDetailSerializers(serializers.ModelSerializer):

    service_imgs = ServiceImageSerializers(many=True)
    service_items = ServiceItemSerializers(many=True)
    service_staff = ServiceStaffSerializers(many=True)

    class Meta:
        model = Service
        fields = "__all__"


class ShopPicSerializers(serializers.ModelSerializer):

    class Meta:
        model = ShopIndexPic
        fields = "__all__"






