from bookapp import models
from .models import Book, User

# 给每一个model类提供序列化

from rest_framework import serializers,exceptions
from django.conf import settings


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    # sex = serializers.IntegerField()
    # icon = serializers.ImageField()
    pwd = serializers.CharField()

    # 字定义序列化属性
    # 属性名随意，函数命由固定的get+_属性名构成（self,参与序列化的model对象obj）
    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        return obj.get_sex_display()

    # 序列化图像
    icon = serializers.SerializerMethodField()
    # obj 为当前序列化对象
    def get_icon(self, obj):
        # print(settings.MEDIA_URL)
        # print(obj.icon, type(obj.icon))
        return '%s%s%s' % (r'http://127.0.0.1:8000', settings.MEDIA_URL, str(obj.icon))


class UserDeSerializer(serializers.Serializer):
    # 可以自定义错误信息
    name = serializers.CharField(max_length=10,min_length=3,error_messages={
        'max_length':"太长",
        'min_length':"太短"
    })
    pwd = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    sex = serializers.CharField(required=False)

    # 自定义有校验规则的序列化字段
    re_pwd = serializers.CharField(required=True)

    # 局部钩子：validate_要校验的字段名(self,当前要校验的字段的值)
    # 校验通过，返回原值，校验失败，抛出异常
    def validate_name(self, value):
        print('value', value)
        if 'j' in value.lower():   #名字中不能存在j，这里仅仅是测试局部验证
            raise exceptions.ValidationError('名字非法')
        return value

    # 全局钩子：validate(self,系统与局部校验全部通过的字段的值)
    def validate(self, attrs):
        pwd = attrs.get('pwd')
        re_pwd = attrs.pop('re_pwd')
        if pwd != re_pwd:
            raise exceptions.ValidationError({'pwd':'两次密码不一样'})
        return attrs

    # 完成新增，需要重写create方法
    def create(self, validated_data):
        # 在所有校验规则完毕之后，数据直接入库
        return models.User.objects.create(**validated_data)
