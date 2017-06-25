# -*- coding: utf-8 -*-
# __author__ = xutao

from rest_framework import serializers
from apps.models import Shop, Service, ShopIndexPic


class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = "__all__"


class ShopServiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"


class ShopPicSerializers(serializers.ModelSerializer):

    class Meta:
        model = ShopIndexPic
        fields = "__all__"