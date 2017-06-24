# -*- coding: utf-8 -*-
# __author__ = xutao

from django.db import models
from django.contrib.contenttypes.models import ContentType
from libs.uuids import create_uuid

# Create your models here.


class CommonModelMixin(models.Model):

    id = models.CharField(u"UID", max_length=36, primary_key=True, default=create_uuid)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s, %s" % (self.__class__.__name__, self.id)

    class Meta:
        abstract = True

    @staticmethod
    def get_instance_info(instance):
        return dict(target_type=instance.__class__.__name__.lower(), target_id=instance.id)

    def get_target_model(self):
        """
            获取 目标 model
        :return: 
        """
        taget = ContentType.objects.get(model=self.target_type)
        return taget.model_class()

    def get_target_obj(self):
        """
            获取 目标 obj
        :return: 
        """
        model = self.get_target_model()
        obj = model.objects.get(id=self.target_id)
        return obj

    @property
    def model_name(self):
        """
            model 名称
        :return: 
        """
        return self.__class__.__name__.lower()

    @classmethod
    def cls_model_name(cls):
        """
            classs name
        :return: 
        """
        return cls.__name__.lower()
