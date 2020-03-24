from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Request, Response
from rest_framework.serializers import Serializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework import status

from bookapp import models, serializers
from bookapp.models import Book


class Health(View):
    def get(self, *args, **kwargs):
        return JsonResponse("ok", safe=False)


class BookView(APIView):
    # 自定义局部解析类配置
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def get(self, request, *args, **kwargs):
        # print(request.GET)   兼容
        # print(request._request.GET)    二次封装
        # print(request.query_params)    拓展URL拼接参数用它取

        return Response({
            "code": "success",
            "data": "haha",
            "msg": "图书",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request._request.POST)
        # 这里如果接受的body参数为form类型，则值为querydict类型
        print(request.data)

        # 获取url拼接参数传参的方式
        # print(request.query_params)
        # print(request.query_params.dict())
        # 测试一下
        # 测试分支
        return Response('post_ok')


class User(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        if pk:
            try:
                user_obj = models.User.objects.get(pk=pk)
                user_ser = serializers.UserSerializer(user_obj)

                return Response({'code': status.HTTP_200_OK,
                                 'msg': '用户列表',
                                 'data': user_ser.data})
            except:
                return Response({
                    'code': status.HTTP_200_OK,
                    'msg': '用户不存在',
                })
        else:
            user_obj_list = models.User.objects.all()
            user_ser_data = serializers.UserSerializer(user_obj_list,many=True).data
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '用户列表',
                'data': user_ser_data,
            })

    def post(self, request, *args, **kwargs):
        request_data = request.data
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                'code': 1,
                'msg': '数据不合法',
            })
        book_ser = serializers.UserDeSerializer(data=request_data)
        if book_ser.is_valid():
            # 数据校验通过,校验成功完成创建
            book_obj = book_ser.save()   #实现validate() create()方法

            return Response({
                'code': status.HTTP_200_OK,
                'msg': '创建成功',
                'data': serializers.UserSerializer(book_obj).data
            })
        else:
            return Response({
                'code':1,
                'msg':book_ser.errors
            })

