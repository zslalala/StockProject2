from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
import json

from .models import StockInfo

# Create your views here.

# #添加书籍的服务
# @require_http_methods(["GET"])
# def add_book(request):
#     response = {}
#     try:
#         book = Book(name=request.GET.get('name'))
#         book.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except  Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)

#获取书籍的服务
@require_http_methods(["GET","POST"])
def show_stock(request):

    data = json.loads(request.body)
    stockid = data.get('stockid')
    startdate = data.get('startdate')
    enddate = data.get('enddate')

    print(startdate+"!!!!!@")

    return JsonResponse({
        "stockid":stockid+"0000",
        "startdate":startdate+"1111",
        "enddate":enddate+"2222"
    })


def detail(request, id):
    return HttpResponse("You're looking at Student %s." % id)