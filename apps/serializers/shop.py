# -*- coding: utf-8 -*-
# __author__ = xutao

from rest_framework import serializers
from apps.models import Shop, Service, ShopIndexPic, ServiceImage


class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = "__all__"


class ShopServiceListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"
        exclude = ("service_imgs", )


class ShopServiceDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"


class ShopPicSerializers(serializers.ModelSerializer):

    class Meta:
        model = ShopIndexPic
        fields = "__all__"


class ServiceImageSerializers(serializers.ModelSerializer):


    class Meta:
        model = ServiceImage
        fields = "__all__"