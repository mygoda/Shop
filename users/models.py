# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django_extensions.db.fields.json import JSONField


from users.managers import UserManager
from libs.datetimes import datetime_now
from libs.uuids import create_uuid, create_sms_code
import time
import logging
from libs.errors import ServerError
from django.conf import settings

logger = logging.getLogger("hair")

__all__ = ["User", "Customer", "Staff", "AccessToken"]


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "user"
        verbose_name = verbose_name_plural = u"后台管理用户"

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = (
        (GENDER_MALE, '男'),
        (GENDER_FEMALE, '女'),
    )

    USER_TYPE = (
        ("customer", u"用户"),
        (u"staff", "工作人员")
    )

    id = models.AutoField(u"用户认证", primary_key=True, unique=True)
    email = models.EmailField(u"邮箱", max_length=255, default="", blank=True, null=True)
    username = models.CharField(u"用户名", max_length=32, default="", blank=True, null=True)
    avatar = models.CharField(u"头像", max_length=255, blank=True, null=True)
    phone = models.CharField(u"手机号", max_length=24, blank=True, null=True, default="")
    gender = models.SmallIntegerField(u"性别", default=GENDER_FEMALE, choices=GENDER_CHOICES)
    is_active = models.BooleanField(u"是否有效", default=True)
    is_admin = models.BooleanField(u"是否管理员", default=False)
    is_staff = models.BooleanField(u"是否工作人员", default=False)
    wechat = models.CharField(u"wechat", max_length=36, null=True, blank=True)
    created_at = models.DateTimeField(u"创建时间", blank=True, null=True, default=datetime_now)
    is_valid = models.BooleanField(u"是否有效", default=True)
    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ["email", ]

    def get_username(self):
        return self.get_full_name()

    def get_full_name(self):
        return "%s" % self.username

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.get_full_name()

    @classmethod
    def get_user_by_phone(cls, phone):
        users = User.objects.filter(phone=phone)
        try:
            # 返回第一个用户
            return users[0]
        except:
            return None


class Customer(models.Model):
    """
        客户
    """
    class Meta:
        verbose_name = verbose_name_plural = u"用户"

    wechat = models.CharField(u"微信号", null=True, blank=True, max_length=32)
    name = models.CharField(u"名字", max_length=16, null=True, blank=True)
    uuid = models.CharField(u"微信号", null=True, blank=True, max_length=36)
    nickname = models.CharField(u"微信昵称", max_length=36, null=True, blank=True)
    age = models.IntegerField(u"年龄", default=10)
    phone = models.CharField(u"电话号", max_length=13, blank=True, null=True)
    gender = models.CharField(u"性别", max_length=4, null=True, blank=True, default=u"女")

    is_valid = models.BooleanField(u"是否有效", default=True)
    created_at = models.DateTimeField(u"创建时间", blank=True, null=True, default=datetime_now)

    def __unicode__(self):
        return self.nickname


class AccessToken(models.Model):
    """
        access token
    """
    class Meta:
        verbose_name = verbose_name_plural = u"登录令牌"

    customer = models.ForeignKey(Customer, verbose_name=u"客户")
    access_token = models.CharField(max_length=36, default=create_uuid)
    create_timestamp = models.IntegerField(u"创建时间", default=0)
    expired_timestamp = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s-%s" % (self.access_token, self.customer.name)

    @classmethod
    def get_user_by_token(cls, token=""):
        """
            根据 token 获取用户
        :param token:
        :return:
        """
        now = time.time()
        has_user = cls.objects.filter(access_token=token, expired_timestamp__gt=now).exists()
        if not has_user:
            raise ServerError(0)
        access_token = cls.objects.filter(access_token=token, expired_timestamp__gt=now).order_by("-create_timestamp")[0]
        return access_token.user

    @classmethod
    def generate_user_access_token(cls, user):
        """
            生成 access token
        :param user:
        :return:
        """
        EXPIRED_TIME = settings.EXPIRED_TIME  # 默认过期时间为一天
        logger.info("start generate %s access token" % user.nickname)
        now = time.time()
        expried_time = now + EXPIRED_TIME
        user_access_token = cls(user_id=user.id, expired_timestamp=expried_time, create_timestamp=now)
        user_access_token.save()
        logger.info("start generate %s access token %s" % (user.nickname, user_access_token.access_token))


class SmsCode(models.Model):
    """
        手机
    """
    class Meta:
        verbose_name = verbose_name_plural = u"手机验证码"

    ACTION = (
        ("register", u"注册"),
        ("delete", u"删除"),
    )

    code = models.CharField(u"验证码", max_length=8, default=create_sms_code)
    type = models.CharField(u"类型", max_length=16, default="register", choices=ACTION)
    mobile = models.CharField(u"手机号码", max_length=24)
    create_timestamp = models.IntegerField(u"创建时间", default=0)
    is_valid = models.BooleanField(u"是否有效", default=True)
    expired_time = models.IntegerField(u"过期时间", default=30 * 60)  # 过期时间默认为 30 分钟

    def __unicode__(self):
        return "%s:%s" % (self.code, self.mobile)

    @classmethod
    def check_valid(cls, code, mobile, type="register"):
        """
            查看 验证码是否有效
        :param code:
        :param mobile:
        :param type:
        :return:
        """
        now = time.time()
        logger.info("start valid mobile %s code %s in %s time %s" % (mobile, code, type, now))
        if cls.objects.filter(mobile=mobile, code=code, type=type, is_valid=True).exists():
            sms_code = cls.objects.filter(mobile=mobile, code=code, type=type).order_by("-create_timestamp")[0]
            if now > sms_code.create_timestamp + sms_code.expired_time:
                return False
            else:
                # 使用过了 设置为无效
                sms_code.is_valid = False
                sms_code.save()
                return True
        return False
