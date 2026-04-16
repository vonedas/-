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


#  定义上传文件方法
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


#    定义添加公告的方法，响应页面请求
def addnotice(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加公告页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addnotice.html', {});


#  处理添加公告方法   
def addnoticeact(request):
    #  从页面post数据中获取标题
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  调用uploadFile方法上传页面中图片
    pic = uploadFile(request, "picfile");

    #  从页面post数据中获取内容
    neirongstr = request.POST.get("neirong");
    neirong = "";
    if (neirongstr is not None):
        neirong = neirongstr;

    #  从页面post数据中获取时间
    shijianstr = request.POST.get("shijian");
    shijian = "";
    if (shijianstr is not None):
        shijian = shijianstr;

    #  将公告的属性赋值给公告，生成公告对象
    notice = models.Notice(name=name, pic=pic, neirong=neirong, shijian=shijian, );

    #  调用save方法保存公告信息
    notice.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加公告成功,并跳转到公告管理页面
    return HttpResponse(u"<p>添加公告成功</p><a href='/notice/noticemanage'>返回页面</a>");


#  定义表名管理方法，响应页面noticemanage请求   
def noticemanage(request):
    #  通过all方法查询所有的公告信息
    noticeall = models.Notice.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到公告管理页面，并附带所有公告信息
    return render(request, 'xitong/noticemanage.html', {'noticeall': noticeall});


#  定义表名查看方法，响应页面noticeview请求   
def noticeview(request):
    #  通过all方法查询所有的公告信息
    noticeall = models.Notice.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到公告查看页面，并附带所有公告信息
    return render(request, 'xitong/noticeview.html', {'noticeall': noticeall});


#  定义修改公告方法，通过id查询对应的公告信息，返回页面展示  
def updatenotice(request, id):
    #  使用get方法，通过id查询对应的公告信息
    notice = models.Notice.objects.get(id=id);

    #  跳转到修改公告页面，并附带当前公告信息
    return render(request, 'xitong/updatenotice.html', {'notice': notice, });


#  定义处理修改公告方法   
def updatenoticeact(request):
    #  使用request获取post中的公告id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的公告id获取对应的公告信息
    notice = models.Notice.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给notice的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        notice.name = namestr;

    #  调用uploadFile方法上传页面中图片
    picfile = uploadFile(request, "picfile");

    #  如果picfile不等于false
    if (picfile != "false"):
        #  将picfile赋值给公告的图片字段
        notice.pic = picfile;

    #  从页面post数据中获取内容并赋值给notice的neirong字段
    neirongstr = request.POST.get("neirong");
    if (neirongstr is not None):
        notice.neirong = neirongstr;

    #  从页面post数据中获取时间并赋值给notice的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        notice.shijian = shijianstr;

    #  调用save方法保存公告信息
    notice.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改公告成功,并跳转到公告管理页面
    return HttpResponse(u"<p>修改公告成功</p><a href='/notice/noticemanage'>返回页面</a>");


#  定义删除公告方法   
def deletenoticeact(request, id):
    #  调用django的delete方法，根据id删除公告信息
    models.Notice.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除公告成功,并跳转到公告管理页面
    return HttpResponse(u"<p>删除公告成功</p><a href='/notice/noticemanage'>返回页面</a>");


#  定义搜索公告方法，响应页面搜索请求   
def searchnotice(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的公告信息
    noticeall = models.Notice.objects.filter(name__icontains=search);

    #  跳转到搜索公告页面，并附带查询的公告信息
    return render(request, 'xitong/searchnotice.html', {"noticeall": noticeall});


#  处理公告详情   
def noticedetails(request, id):
    #  根据页面传入id获取公告信息
    notice = models.Notice.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到公告详情页面,并公告信息传递到页面中
    return render(request, 'xitong/noticedetails.html', {"notice": notice});


#  处理添加公告Json方法
def addnoticeactjson(request):
    result = {};
    # 从request中获取标题信息
    name = getQuery(request, "name");
    # 从request中获取图片信息
    pic = getQuery(request, "pic");
    # 从request中获取内容信息
    neirong = getQuery(request, "neirong");
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");

    #  将公告的属性赋值给公告，生成公告对象
    notice = models.Notice(name=name, pic=pic, neirong=neirong, shijian=shijian, );

    #  调用save方法保存公告信息
    notice.save();
    result['message'] = "添加公告成功"
    result['code'] = "202"

    #  返回添加公告的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改公告方法   
def updatenoticeactjson(request):
    result = {};

    #  使用request获取post中的公告id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的公告id获取对应的公告信息
    notice = models.Notice.objects.get(id=id);
    # 从request中获取标题信息
    name = getQuery(request, "name");
    # 如果request中存在标题信息，赋值给公告
    if (name != ""):
        notice.name = name;
    # 从request中获取图片信息
    pic = getQuery(request, "pic");
    # 如果request中存在图片信息，赋值给公告
    if (pic != ""):
        notice.pic = pic;
    # 从request中获取内容信息
    neirong = getQuery(request, "neirong");
    # 如果request中存在内容信息，赋值给公告
    if (neirong != ""):
        notice.neirong = neirong;
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 如果request中存在时间信息，赋值给公告
    if (shijian != ""):
        notice.shijian = shijian;

    #  调用save方法保存公告信息
    notice.save();
    result['message'] = "修改公告成功"
    result['code'] = "202"

    #  返回修改公告的结果
    return HttpResponse(json.dumps(result));


#  定义删除公告方法   
def deletenoticejson(request):
    result = {};

    #  使用request获取post中的公告id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除公告信息
    models.Notice.objects.filter(id=id).delete();
    result['message'] = "删除公告成功"
    result['code'] = "202"

    #  返回删除公告的结果
    return HttpResponse(json.dumps(result));


#  定义搜索公告json方法，响应页面搜索请求   
def searchnoticejson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的公告信息
    noticeall = models.Notice.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的公告信息
    result['noticeall'] = objtodic(noticeall)
    result['message'] = "查询公告成功"
    result['code'] = "202"

    #  返回查询公告的结果
    return HttpResponse(json.dumps(result));


#  处理公告详情   
def noticedetailsjson(request):
    result = {};

    #  使用request获取post中的公告id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取公告信息
    notice = models.Notice.objects.get(id=id);
    result['notice'] = objtodic(notice);
    result['message'] = "查询公告成功"
    result['code'] = "202"

    #  返回查询公告详情的结果
    return HttpResponse(json.dumps(result));
