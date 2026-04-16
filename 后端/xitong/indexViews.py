# coding:utf-8
from django.db.models import QuerySet
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse
from . import models
import random, os, json;


def uploadFile(request, filename):
    #  获取传入的文件信息
    file_obj = request.FILES.get(filename)

    #  如果传入的文件为空，则返回false
    if file_obj == None:
        return "false"

    #  获取该文件的后缀信息
    houzhui = file_obj.name.split(".")[-1];
    # 写入文件
    file_name = 'temp_file-%d' % random.randint(0, 100000) + "." + houzhui  # 不能使用文件名称，因为存在中文，会引起内部错误
    file_full_path = os.path.join("static/upload/", file_name)
    dest = open(file_full_path, 'wb+')
    dest.write(file_obj.read())
    dest.close()

    #  返回文件的名字
    return file_name;


# 定义获取数据方法
def getQuery(request, name):
    # 定义返回数据初始值
    result = "";

    # 尝试从GET参数中获取数据
    if (request.GET.get(name) is not None):
        # 如果GET中存在数据，则返回GET中的数据信息
        result = request.GET.get(name);
    # 尝试从POST参数中获取数据
    elif (request.POST.get(name) is not None):
        # 如果POST中存在数据，则返回POST中的数据信息
        result = request.POST.get(name);
    else:
        # 从request的body中获取数据
        try:
            json_str = request.body  # 属性获取最原始的请求体数据
            json_dict = json.loads(json_str)  # 将原始数据转成字典格式
            result = json_dict.get(name)  # 获取数据
        except:
            pass;

    # 返回数据信息
    return result;


# 将Django的模型对象转换为字典信息
def objtodic(obj):
    # 如果obj是QuerySet类，则遍历转换
    if (type(obj) == QuerySet):
        result = [];
        # 进行遍历并转换对象为字典
        for i in obj:
            result.append(i.todic())

        # 返回转换结果
        return result;
    else:
        # 返回转换结果
        return obj.todic();


def index(request):
    #  从notice中获取最新的6条数据
    noticezuixin6 = models.Notice.objects.order_by('-id')[:6];

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");
    return render(request, 'xitong/index.html', {"noticezuixin6": noticezuixin6, });


import datetime


def indexjson(request):
    result = {}
    print(request.GET.get("userid"))
    userid = request.GET.get('userid');
    print(userid)
    #  从notice中获取最新的6条数据
    noticezuixin6 = models.Notice.objects.order_by('-id')[:6];
    result['noticezuixin6'] = objtodic(noticezuixin6);

    user = models.User.objects.get(id=userid)

    if (user.tizhong):
        tizhong = user.tizhong
    else:
        tizhong = 0

    result['tizhong'] = tizhong;

    today = datetime.date.today()
    today = today.strftime("%Y-%m-%d")

    # models.Yinshilog.objects.
    # 进行查询
    today_records = models.Yinshilog.objects.filter(
        shijian=today,  # 如果是 DateTimeField 类型，使用 __date 来提取日期部分进行比较
        userid=userid
    );
    eatkaluli = 0
    for yinshilog in today_records:
        data = yinshilog.todic();
        try:
            if data['kaluli'] and data['kaluli'].isdigit():
                eatkaluli = eatkaluli + int(data['kaluli'])
        except (ValueError, KeyError):
            continue
    result['eatkaluli'] = eatkaluli;

    today_records = models.Duanlianlog.objects.filter(
        shijian=today,  # 如果是 DateTimeField 类型，使用 __date 来提取日期部分进行比较
        userid=userid
    );

    duanliankaluli = 0
    for duanlianlog in today_records:
        data = duanlianlog.todic()
        duanliankaluli = duanliankaluli + int(data['kaluli'])
    result['duanliankaluli'] = duanliankaluli;

    today_records = models.Yao.objects.filter(userid=userid);
    # result['yao'] = yao;
    # today_records = models.Duanlianlog.objects.filter(
    #     shijian=today,  # 如果是 DateTimeField 类型，使用 __date 来提取日期部分进行比较
    #     userid=userid
    # );

    yaoarr = []
    for duanlian in today_records:
        data = duanlian.todic();
        yaoarr.append(data);
    # print(today_records);
    result['yao'] = yaoarr;

    result['code'] = "202"

    #  返回查询公告的结果
    return HttpResponse(json.dumps(result));
