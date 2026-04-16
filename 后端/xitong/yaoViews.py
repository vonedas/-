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


#    定义添加吃药提醒的方法，响应页面请求
def addyao(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加吃药提醒页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addyao.html', {'userall': userall, });


#  处理添加吃药提醒方法   
def addyaoact(request):
    #  从页面post数据中获取标题
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取用户
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取用户id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取时间
    shijianstr = request.POST.get("shijian");
    shijian = "";
    if (shijianstr is not None):
        shijian = shijianstr;

    #  将吃药提醒的属性赋值给吃药提醒，生成吃药提醒对象
    yao = models.Yao(name=name, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存吃药提醒信息
    yao.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加吃药提醒成功,并跳转到吃药提醒管理页面
    return HttpResponse(u"<p>添加吃药提醒成功</p><a href='/yao/yaomanage'>返回页面</a>");


#  定义表名管理方法，响应页面yaomanage请求   
def yaomanage(request):
    #  通过all方法查询所有的吃药提醒信息
    yaoall = models.Yao.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到吃药提醒管理页面，并附带所有吃药提醒信息
    return render(request, 'xitong/yaomanage.html', {'yaoall': yaoall});


#  定义表名查看方法，响应页面yaoview请求   
def yaoview(request):
    #  通过all方法查询所有的吃药提醒信息
    yaoall = models.Yao.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到吃药提醒查看页面，并附带所有吃药提醒信息
    return render(request, 'xitong/yaoview.html', {'yaoall': yaoall});


#  定义修改吃药提醒方法，通过id查询对应的吃药提醒信息，返回页面展示  
def updateyao(request, id):
    #  使用get方法，通过id查询对应的吃药提醒信息
    yao = models.Yao.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改吃药提醒页面，并附带当前吃药提醒信息
    return render(request, 'xitong/updateyao.html', {'yao': yao, 'userall': userall, });


#  定义处理修改吃药提醒方法   
def updateyaoact(request):
    #  使用request获取post中的吃药提醒id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的吃药提醒id获取对应的吃药提醒信息
    yao = models.Yao.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给yao的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        yao.name = namestr;

    #  从页面post数据中获取用户并赋值给yao的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        yao.user = userstr;

    #  从页面post数据中获取用户id并赋值给yao的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        yao.userid = useridstr;

    #  从页面post数据中获取时间并赋值给yao的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        yao.shijian = shijianstr;

    #  调用save方法保存吃药提醒信息
    yao.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改吃药提醒成功,并跳转到吃药提醒管理页面
    return HttpResponse(u"<p>修改吃药提醒成功</p><a href='/yao/yaomanage'>返回页面</a>");


#  定义删除吃药提醒方法   
def deleteyaoact(request, id):
    #  调用django的delete方法，根据id删除吃药提醒信息
    models.Yao.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除吃药提醒成功,并跳转到吃药提醒管理页面
    return HttpResponse(u"<p>删除吃药提醒成功</p><a href='/yao/yaomanage'>返回页面</a>");


#  定义搜索吃药提醒方法，响应页面搜索请求   
def searchyao(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的吃药提醒信息
    yaoall = models.Yao.objects.filter(name__icontains=search);

    #  跳转到搜索吃药提醒页面，并附带查询的吃药提醒信息
    return render(request, 'xitong/searchyao.html', {"yaoall": yaoall});


#  处理吃药提醒详情   
def yaodetails(request, id):
    #  根据页面传入id获取吃药提醒信息
    yao = models.Yao.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到吃药提醒详情页面,并吃药提醒信息传递到页面中
    return render(request, 'xitong/yaodetails.html', {"yao": yao});


#  处理添加吃药提醒Json方法
def addyaoactjson(request):
    result = {};
    # 从request中获取标题信息
    name = getQuery(request, "name");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");

    #  将吃药提醒的属性赋值给吃药提醒，生成吃药提醒对象
    yao = models.Yao(name=name, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存吃药提醒信息
    yao.save();
    result['message'] = "添加吃药提醒成功"
    result['code'] = "202"

    #  返回添加吃药提醒的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改吃药提醒方法   
def updateyaoactjson(request):
    result = {};

    #  使用request获取post中的吃药提醒id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的吃药提醒id获取对应的吃药提醒信息
    yao = models.Yao.objects.get(id=id);
    # 从request中获取标题信息
    name = getQuery(request, "name");
    # 如果request中存在标题信息，赋值给吃药提醒
    if (name != ""):
        yao.name = name;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给吃药提醒
    if (user != ""):
        yao.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给吃药提醒
    if (userid != ""):
        yao.userid = userid;
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 如果request中存在时间信息，赋值给吃药提醒
    if (shijian != ""):
        yao.shijian = shijian;
    # 从request中获取打卡信息
    daka = getQuery(request, "daka");
    # 如果request中存在打卡信息，赋值给吃药提醒
    if (daka != ""):
        yao.daka = daka;

    #  调用save方法保存吃药提醒信息
    yao.save();
    result['message'] = "修改吃药提醒成功"
    result['code'] = "202"

    #  返回修改吃药提醒的结果
    return HttpResponse(json.dumps(result));


#  定义删除吃药提醒方法   
def deleteyaojson(request):
    result = {};

    #  使用request获取post中的吃药提醒id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除吃药提醒信息
    models.Yao.objects.filter(id=id).delete();
    result['message'] = "删除吃药提醒成功"
    result['code'] = "202"

    #  返回删除吃药提醒的结果
    return HttpResponse(json.dumps(result));


#  定义搜索吃药提醒json方法，响应页面搜索请求   
def searchyaojson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的吃药提醒信息
    yaoall = models.Yao.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的吃药提醒信息
    result['yaoall'] = objtodic(yaoall)
    result['message'] = "查询吃药提醒成功"
    result['code'] = "202"

    #  返回查询吃药提醒的结果
    return HttpResponse(json.dumps(result));


#  处理吃药提醒详情   
def yaodetailsjson(request):
    result = {};

    #  使用request获取post中的吃药提醒id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取吃药提醒信息
    yao = models.Yao.objects.get(id=id);
    result['yao'] = objtodic(yao);
    result['message'] = "查询吃药提醒成功"
    result['code'] = "202"

    #  返回查询吃药提醒详情的结果
    return HttpResponse(json.dumps(result));
