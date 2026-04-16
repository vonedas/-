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


#    定义添加体重的方法，响应页面请求
def addtizhong(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加体重页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addtizhong.html', {'userall': userall, });


#  处理添加体重方法   
def addtizhongact(request):
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

    shujustr = request.POST.get("shuju");
    shuju = "";
    if (shujustr is not None):
        shuju = shujustr;

    #  将体重的属性赋值给体重，生成体重对象
    tizhong = models.Tizhong(name=name, user=user, userid=userid, shijian=shijian, shuju=shuju);

    #  调用save方法保存体重信息
    tizhong.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加体重成功,并跳转到体重管理页面
    return HttpResponse(u"<p>添加体重成功</p><a href='/tizhong/tizhongmanage'>返回页面</a>");


#  定义表名管理方法，响应页面tizhongmanage请求   
def tizhongmanage(request):
    #  通过all方法查询所有的体重信息
    tizhongall = models.Tizhong.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到体重管理页面，并附带所有体重信息
    return render(request, 'xitong/tizhongmanage.html', {'tizhongall': tizhongall});


#  定义表名查看方法，响应页面tizhongview请求   
def tizhongview(request):
    #  通过all方法查询所有的体重信息
    tizhongall = models.Tizhong.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到体重查看页面，并附带所有体重信息
    return render(request, 'xitong/tizhongview.html', {'tizhongall': tizhongall});


#  定义修改体重方法，通过id查询对应的体重信息，返回页面展示  
def updatetizhong(request, id):
    #  使用get方法，通过id查询对应的体重信息
    tizhong = models.Tizhong.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改体重页面，并附带当前体重信息
    return render(request, 'xitong/updatetizhong.html', {'tizhong': tizhong, 'userall': userall, });


#  定义处理修改体重方法   
def updatetizhongact(request):
    #  使用request获取post中的体重id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的体重id获取对应的体重信息
    tizhong = models.Tizhong.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给tizhong的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        tizhong.name = namestr;

    #  从页面post数据中获取用户并赋值给tizhong的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        tizhong.user = userstr;

    #  从页面post数据中获取用户id并赋值给tizhong的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        tizhong.userid = useridstr;

    #  从页面post数据中获取时间并赋值给tizhong的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        tizhong.shijian = shijianstr;

    #  调用save方法保存体重信息
    tizhong.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改体重成功,并跳转到体重管理页面
    return HttpResponse(u"<p>修改体重成功</p><a href='/tizhong/tizhongmanage'>返回页面</a>");


#  定义删除体重方法   
def deletetizhongact(request, id):
    #  调用django的delete方法，根据id删除体重信息
    models.Tizhong.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除体重成功,并跳转到体重管理页面
    return HttpResponse(u"<p>删除体重成功</p><a href='/tizhong/tizhongmanage'>返回页面</a>");


#  定义搜索体重方法，响应页面搜索请求   
def searchtizhong(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的体重信息
    tizhongall = models.Tizhong.objects.filter(name__icontains=search);

    #  跳转到搜索体重页面，并附带查询的体重信息
    return render(request, 'xitong/searchtizhong.html', {"tizhongall": tizhongall});


#  处理体重详情   
def tizhongdetails(request, id):
    #  根据页面传入id获取体重信息
    tizhong = models.Tizhong.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到体重详情页面,并体重信息传递到页面中
    return render(request, 'xitong/tizhongdetails.html', {"tizhong": tizhong});


#  定义跳转user添加体重页面的方法  
def useraddtizhong(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加体重页面
    return render(request, 'xitong/useraddtizhong.html', {'userall': userall, });


#  处理添加体重方法   
def useraddtizhongact(request):
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

    #  将体重的属性赋值给体重，生成体重对象
    tizhong = models.Tizhong(name=name, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存体重信息
    tizhong.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加体重成功,并跳转到体重管理页面
    return HttpResponse(u"<p>添加体重成功</p><a href='/tizhong/usertizhongmanage'>返回页面</a>");


#  跳转user体重管理页面
def usertizhongmanage(request):
    #  查询出userid等于当前用户id的所有体重信息
    tizhongall = models.Tizhong.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回体重管理页面，并携带tizhongall的数据信息
    return render(request, 'xitong/usertizhongmanage.html', {'tizhongall': tizhongall});


#  定义跳转user修改体重页面      
def userupdatetizhong(request, id):
    #  根据页面传入的体重id信息，查询出对应的体重信息
    tizhong = models.Tizhong.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改体重页面，并携带查询出的体重信息
    return render(request, 'xitong/userupdatetizhong.html', {'tizhong': tizhong, 'userall': userall, });


#  定义处理修改体重方法   
def userupdatetizhongact(request):
    #  使用request获取post中的体重id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的体重id获取对应的体重信息
    tizhong = models.Tizhong.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给tizhong的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        tizhong.name = namestr;

    #  从页面post数据中获取用户并赋值给tizhong的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        tizhong.user = userstr;

    #  从页面post数据中获取用户id并赋值给tizhong的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        tizhong.userid = useridstr;

    #  从页面post数据中获取时间并赋值给tizhong的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        tizhong.shijian = shijianstr;

    #  调用save方法保存体重信息
    tizhong.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改体重成功,并跳转到体重管理页面
    return HttpResponse(u"<p>修改体重成功</p><a href='/tizhong/usertizhongmanage'>返回页面</a>");


#  定义user删除体重信息
def userdeletetizhongact(request, id):
    #  根据页面传入的体重id信息，删除出对应的体重信息
    models.Tizhong.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除体重成功，并跳转到体重管理页面
    return HttpResponse(u"<p>删除体重成功</p><a href='/tizhong/usertizhongmanage'>返回页面</a>");


#  处理添加体重Json方法
def addtizhongactjson(request):
    result = {};
    # 从request中获取标题信息
    name = getQuery(request, "name");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");

    #  将体重的属性赋值给体重，生成体重对象
    tizhong = models.Tizhong(name=name, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存体重信息
    tizhong.save();
    result['message'] = "添加体重成功"
    result['code'] = "202"

    #  返回添加体重的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改体重方法   
def updatetizhongactjson(request):
    result = {};

    #  使用request获取post中的体重id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的体重id获取对应的体重信息
    tizhong = models.Tizhong.objects.get(id=id);
    # 从request中获取标题信息
    name = getQuery(request, "name");
    # 如果request中存在标题信息，赋值给体重
    if (name != ""):
        tizhong.name = name;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给体重
    if (user != ""):
        tizhong.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给体重
    if (userid != ""):
        tizhong.userid = userid;
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 如果request中存在时间信息，赋值给体重
    if (shijian != ""):
        tizhong.shijian = shijian;

    #  调用save方法保存体重信息
    tizhong.save();
    result['message'] = "修改体重成功"
    result['code'] = "202"

    #  返回修改体重的结果
    return HttpResponse(json.dumps(result));


#  定义删除体重方法   
def deletetizhongjson(request):
    result = {};

    #  使用request获取post中的体重id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除体重信息
    models.Tizhong.objects.filter(id=id).delete();
    result['message'] = "删除体重成功"
    result['code'] = "202"

    #  返回删除体重的结果
    return HttpResponse(json.dumps(result));


#  定义搜索体重json方法，响应页面搜索请求   
def searchtizhongjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的体重信息
    tizhongall = models.Tizhong.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的体重信息
    result['tizhongall'] = objtodic(tizhongall)
    result['message'] = "查询体重成功"
    result['code'] = "202"

    #  返回查询体重的结果
    return HttpResponse(json.dumps(result));


#  处理体重详情   
def tizhongdetailsjson(request):
    result = {};

    #  使用request获取post中的体重id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取体重信息
    tizhong = models.Tizhong.objects.get(id=id);
    result['tizhong'] = objtodic(tizhong);
    result['message'] = "查询体重成功"
    result['code'] = "202"

    #  返回查询体重详情的结果
    return HttpResponse(json.dumps(result));
