# -*- coding: utf-8 -*-
# __author__ = xutao

from rest_framework import viewsets
from rest_framework.response import Response
from apps.models import Company, Shop, Service, ShopIndexPic
from apps.serializers.shop import ShopSerializers, ShopServiceSerializers, ShopPicSerializers


class ShopViewset(viewsets.ModelViewSet):

    serializer_class = ShopSerializers

    def get_queryset(self):
        return Shop.objects.filter(is_valid=True)

    def list(self, request, *args, **kwargs):
        params = self.request.query_params
        company_id = params.get("c_id")
        if not company_id:
            # 为了测试
            company_id = Company.objects.all()[0].id

        queryset = self.get_queryset().filter(company_id=company_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceViewset(viewsets.ModelViewSet):

    serializer_class = ShopServiceSerializers

    def get_queryset(self):
        return Service.objects.filter(is_valid=True)

    def list(self, request, *args, **kwargs):
        params = self.request.query_params
        shop_id = params.get("shop_id")
        queryset = self.get_queryset().filter(shop_id=shop_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ShopPicViewset(viewsets.ModelViewSet):

    serializer_class = ShopPicSerializers

    def get_queryset(self):
        return ShopIndexPic.objects.all()

    def list(self, request, *args, **kwargs):
        params = self.request.query_params
        shop_id = params.get("shop_id")
        queryset = self.get_queryset().filter(shop_id=shop_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

