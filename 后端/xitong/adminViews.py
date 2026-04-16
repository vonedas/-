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


#    定义添加管理员的方法，响应页面请求
def addadmin(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加管理员页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addadmin.html', {});


#  处理添加管理员方法   
def addadminact(request):
    #  从页面post数据中获取账号
    usernamestr = request.POST.get("username");
    username = "";
    if (usernamestr is not None):
        username = usernamestr;

    #  从页面post数据中获取密码
    passwordstr = request.POST.get("password");
    password = "";
    if (passwordstr is not None):
        password = passwordstr;

    #  将管理员的属性赋值给管理员，生成管理员对象
    admin = models.Admin(username=username, password=password, );

    #  调用save方法保存管理员信息
    admin.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加管理员成功,并跳转到管理员管理页面
    return HttpResponse(u"<p>添加管理员成功</p><a href='/admin/adminmanage'>返回页面</a>");


#  定义表名管理方法，响应页面adminmanage请求   
def adminmanage(request):
    #  通过all方法查询所有的管理员信息
    adminall = models.Admin.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到管理员管理页面，并附带所有管理员信息
    return render(request, 'xitong/adminmanage.html', {'adminall': adminall});


#  定义表名查看方法，响应页面adminview请求   
def adminview(request):
    #  通过all方法查询所有的管理员信息
    adminall = models.Admin.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到管理员查看页面，并附带所有管理员信息
    return render(request, 'xitong/adminview.html', {'adminall': adminall});


#  定义修改管理员方法，通过id查询对应的管理员信息，返回页面展示  
def updateadmin(request, id):
    #  使用get方法，通过id查询对应的管理员信息
    admin = models.Admin.objects.get(id=id);

    #  跳转到修改管理员页面，并附带当前管理员信息
    return render(request, 'xitong/updateadmin.html', {'admin': admin, });


#  定义处理修改管理员方法   
def updateadminact(request):
    #  使用request获取post中的管理员id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的管理员id获取对应的管理员信息
    admin = models.Admin.objects.get(id=id);

    #  从页面post数据中获取账号并赋值给admin的username字段
    usernamestr = request.POST.get("username");
    if (usernamestr is not None):
        admin.username = usernamestr;

    #  从页面post数据中获取密码并赋值给admin的password字段
    passwordstr = request.POST.get("password");
    if (passwordstr is not None):
        admin.password = passwordstr;

    #  调用save方法保存管理员信息
    admin.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改管理员成功,并跳转到管理员管理页面
    return HttpResponse(u"<p>修改管理员成功</p><a href='/admin/adminmanage'>返回页面</a>");


#  定义删除管理员方法   
def deleteadminact(request, id):
    #  调用django的delete方法，根据id删除管理员信息
    models.Admin.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除管理员成功,并跳转到管理员管理页面
    return HttpResponse(u"<p>删除管理员成功</p><a href='/admin/adminmanage'>返回页面</a>");


#  定义搜索管理员方法，响应页面搜索请求   
def searchadmin(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的管理员信息
    adminall = models.Admin.objects.filter(username__icontains=search);

    #  跳转到搜索管理员页面，并附带查询的管理员信息
    return render(request, 'xitong/searchadmin.html', {"adminall": adminall});


#  处理管理员详情   
def admindetails(request, id):
    #  根据页面传入id获取管理员信息
    admin = models.Admin.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到管理员详情页面,并管理员信息传递到页面中
    return render(request, 'xitong/admindetails.html', {"admin": admin});


#  处理添加管理员Json方法
def addadminactjson(request):
    result = {};
    # 从request中获取账号信息
    username = getQuery(request, "username");
    # 从request中获取密码信息
    password = getQuery(request, "password");

    #  将管理员的属性赋值给管理员，生成管理员对象
    admin = models.Admin(username=username, password=password, );

    #  调用save方法保存管理员信息
    admin.save();
    result['message'] = "添加管理员成功"
    result['code'] = "202"

    #  返回添加管理员的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改管理员方法   
def updateadminactjson(request):
    result = {};

    #  使用request获取post中的管理员id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的管理员id获取对应的管理员信息
    admin = models.Admin.objects.get(id=id);
    # 从request中获取账号信息
    username = getQuery(request, "username");
    # 如果request中存在账号信息，赋值给管理员
    if (username != ""):
        admin.username = username;
    # 从request中获取密码信息
    password = getQuery(request, "password");
    # 如果request中存在密码信息，赋值给管理员
    if (password != ""):
        admin.password = password;

    #  调用save方法保存管理员信息
    admin.save();
    result['message'] = "修改管理员成功"
    result['code'] = "202"

    #  返回修改管理员的结果
    return HttpResponse(json.dumps(result));


#  定义删除管理员方法   
def deleteadminjson(request):
    result = {};

    #  使用request获取post中的管理员id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除管理员信息
    models.Admin.objects.filter(id=id).delete();
    result['message'] = "删除管理员成功"
    result['code'] = "202"

    #  返回删除管理员的结果
    return HttpResponse(json.dumps(result));


#  定义搜索管理员json方法，响应页面搜索请求   
def searchadminjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的管理员信息
    adminall = models.Admin.objects.filter(username__icontains=search);

    #  返回查询结果，附带查询的管理员信息
    result['adminall'] = objtodic(adminall)
    result['message'] = "查询管理员成功"
    result['code'] = "202"

    #  返回查询管理员的结果
    return HttpResponse(json.dumps(result));


#  处理管理员详情   
def admindetailsjson(request):
    result = {};

    #  使用request获取post中的管理员id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取管理员信息
    admin = models.Admin.objects.get(id=id);
    result['admin'] = objtodic(admin);
    result['message'] = "查询管理员成功"
    result['code'] = "202"

    #  返回查询管理员详情的结果
    return HttpResponse(json.dumps(result));
