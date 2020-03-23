from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models


class Client(APIView):
    """
    获取数据
    name 获取客户端的名称
    score 获取用户输入的分数
    """

    def get(self, request):
        return render(request, 'client.html', locals())

    def post(self, request):
        name = request.POST.get('name')
        score = request.POST.get('score')

        if not name and score:
            return Response({'status': 401, 'msg': '信息不完整'})
        models.Client.objects.create(
            name=name,
            score=score
        )
        return Response({'status': 200, 'msg': '上传成功'})


class Client_Sort(APIView):
    """
    根据当前数据进行排名
    gamer 当前用户的数据
    gamaer_sorted 排名之后的数据
    """

    def get(self, request):
        name = request.GET.get('name')
        gamer = models.Client.objects.get(name=name)
        gamer_sort = models.Client.objects.order_by('-score')

        gamer_list = [str(i) for i in range(1, len(gamer_sort) + 1)]

        gamer_sorted = dict(zip(gamer_list, gamer_sort))

        return render(request, 'client_sort.html', locals())
