# -*- coding: utf-8 -*-
# __author__ = xutao

from rest_framework import serializers
from apps.models import Shop, Service, ShopIndexPic, ServiceImage


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


class ShopServiceDetailSerializers(serializers.ModelSerializer):

    service_imgs = ServiceImageSerializers(many=True)

    class Meta:
        model = Service
        fields = "__all__"


class ShopPicSerializers(serializers.ModelSerializer):

    class Meta:
        model = ShopIndexPic
        fields = "__all__"


