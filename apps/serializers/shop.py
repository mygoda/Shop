# -*- coding: utf-8 -*-
# __author__ = xutao

from rest_framework import serializers
from apps.models import Shop


class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = "__all__"