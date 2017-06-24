# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from apps.controllers import shop

URL_ID = "(?P<id>[0-9]+)"

schema_view = get_swagger_view(title='理发平台项目接口')

router = routers.DefaultRouter()
router.register(r'shops', shop.ShopViewset, base_name='shops')
router.register(r'services', shop.ServiceViewset, base_name='services')

urlpatterns = [
    # Examples:
    # url(r'^$', 'shops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', schema_view),
]
