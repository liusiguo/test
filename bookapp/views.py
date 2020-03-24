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


class Health(View):
    def get(self, *args, **kwargs):
        return JsonResponse("ok", safe=False)


class Book(APIView):

    # 自定义局部解析类配置
    parser_classes = [JSONParser, FormParser,MultiPartParser]

    def get(self, request, *args, **kwargs):
        # print(request.GET)   兼容
        # print(request._request.GET)    二次封装
        # print(request.query_params)    拓展URL拼接参数用它取

        return Response('restok')

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request._request.POST)
        # 这里如果接受的body参数为form类型，则值为querydict类型
        print(request.data)

        # 获取url拼接参数传参的方式
        # print(request.query_params)
        # print(request.query_params.dict())
        return Response('post_ok')
