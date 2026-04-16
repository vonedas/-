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


#    定义添加饮食记录的方法，响应页面请求
def addyinshilog(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加饮食记录页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addyinshilog.html', {'userall': userall, });


#  处理添加饮食记录方法   
def addyinshilogact(request):
    #  从页面post数据中获取内容
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取卡路里
    kalulistr = request.POST.get("kaluli");
    kaluli = "";
    if (kalulistr is not None):
        kaluli = kalulistr;

    #  从页面post数据中获取时间
    shijianstr = request.POST.get("shijian");
    shijian = "";
    if (shijianstr is not None):
        shijian = shijianstr;

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

    #  将饮食记录的属性赋值给饮食记录，生成饮食记录对象
    yinshilog = models.Yinshilog(name=name, kaluli=kaluli, shijian=shijian, user=user, userid=userid, );

    #  调用save方法保存饮食记录信息
    yinshilog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加饮食记录成功,并跳转到饮食记录管理页面
    return HttpResponse(u"<p>添加饮食记录成功</p><a href='/yinshilog/yinshilogmanage'>返回页面</a>");


#  定义表名管理方法，响应页面yinshilogmanage请求   
def yinshilogmanage(request):
    #  通过all方法查询所有的饮食记录信息
    yinshilogall = models.Yinshilog.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到饮食记录管理页面，并附带所有饮食记录信息
    return render(request, 'xitong/yinshilogmanage.html', {'yinshilogall': yinshilogall});


#  定义表名查看方法，响应页面yinshilogview请求   
def yinshilogview(request):
    #  通过all方法查询所有的饮食记录信息
    yinshilogall = models.Yinshilog.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到饮食记录查看页面，并附带所有饮食记录信息
    return render(request, 'xitong/yinshilogview.html', {'yinshilogall': yinshilogall});


#  定义修改饮食记录方法，通过id查询对应的饮食记录信息，返回页面展示  
def updateyinshilog(request, id):
    #  使用get方法，通过id查询对应的饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改饮食记录页面，并附带当前饮食记录信息
    return render(request, 'xitong/updateyinshilog.html', {'yinshilog': yinshilog, 'userall': userall, });


#  定义处理修改饮食记录方法   
def updateyinshilogact(request):
    #  使用request获取post中的饮食记录id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的饮食记录id获取对应的饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);

    #  从页面post数据中获取内容并赋值给yinshilog的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        yinshilog.name = namestr;

    #  从页面post数据中获取卡路里并赋值给yinshilog的kaluli字段
    kalulistr = request.POST.get("kaluli");
    if (kalulistr is not None):
        yinshilog.kaluli = kalulistr;

    #  从页面post数据中获取时间并赋值给yinshilog的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        yinshilog.shijian = shijianstr;

    #  从页面post数据中获取用户并赋值给yinshilog的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        yinshilog.user = userstr;

    #  从页面post数据中获取用户id并赋值给yinshilog的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        yinshilog.userid = useridstr;

    #  调用save方法保存饮食记录信息
    yinshilog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改饮食记录成功,并跳转到饮食记录管理页面
    return HttpResponse(u"<p>修改饮食记录成功</p><a href='/yinshilog/yinshilogmanage'>返回页面</a>");


#  定义删除饮食记录方法   
def deleteyinshilogact(request, id):
    #  调用django的delete方法，根据id删除饮食记录信息
    models.Yinshilog.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除饮食记录成功,并跳转到饮食记录管理页面
    return HttpResponse(u"<p>删除饮食记录成功</p><a href='/yinshilog/yinshilogmanage'>返回页面</a>");


#  定义搜索饮食记录方法，响应页面搜索请求   
def searchyinshilog(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的饮食记录信息
    yinshilogall = models.Yinshilog.objects.filter(name__icontains=search);

    #  跳转到搜索饮食记录页面，并附带查询的饮食记录信息
    return render(request, 'xitong/searchyinshilog.html', {"yinshilogall": yinshilogall});


#  处理饮食记录详情   
def yinshilogdetails(request, id):
    #  根据页面传入id获取饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到饮食记录详情页面,并饮食记录信息传递到页面中
    return render(request, 'xitong/yinshilogdetails.html', {"yinshilog": yinshilog});


#  定义跳转user添加饮食记录页面的方法  
def useraddyinshilog(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加饮食记录页面
    return render(request, 'xitong/useraddyinshilog.html', {'userall': userall, });


#  处理添加饮食记录方法   
def useraddyinshilogact(request):
    #  从页面post数据中获取内容
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取卡路里
    kalulistr = request.POST.get("kaluli");
    kaluli = "";
    if (kalulistr is not None):
        kaluli = kalulistr;

    #  从页面post数据中获取时间
    shijianstr = request.POST.get("shijian");
    shijian = "";
    if (shijianstr is not None):
        shijian = shijianstr;

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

    #  将饮食记录的属性赋值给饮食记录，生成饮食记录对象
    yinshilog = models.Yinshilog(name=name, kaluli=kaluli, shijian=shijian, user=user, userid=userid, );

    #  调用save方法保存饮食记录信息
    yinshilog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加饮食记录成功,并跳转到饮食记录管理页面
    return HttpResponse(u"<p>添加饮食记录成功</p><a href='/yinshilog/useryinshilogmanage'>返回页面</a>");


#  跳转user饮食记录管理页面
def useryinshilogmanage(request):
    #  查询出userid等于当前用户id的所有饮食记录信息
    yinshilogall = models.Yinshilog.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回饮食记录管理页面，并携带yinshilogall的数据信息
    return render(request, 'xitong/useryinshilogmanage.html', {'yinshilogall': yinshilogall});


#  定义跳转user修改饮食记录页面      
def userupdateyinshilog(request, id):
    #  根据页面传入的饮食记录id信息，查询出对应的饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改饮食记录页面，并携带查询出的饮食记录信息
    return render(request, 'xitong/userupdateyinshilog.html', {'yinshilog': yinshilog, 'userall': userall, });


#  定义处理修改饮食记录方法   
def userupdateyinshilogact(request):
    #  使用request获取post中的饮食记录id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的饮食记录id获取对应的饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);

    #  从页面post数据中获取内容并赋值给yinshilog的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        yinshilog.name = namestr;

    #  从页面post数据中获取卡路里并赋值给yinshilog的kaluli字段
    kalulistr = request.POST.get("kaluli");
    if (kalulistr is not None):
        yinshilog.kaluli = kalulistr;

    #  从页面post数据中获取时间并赋值给yinshilog的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        yinshilog.shijian = shijianstr;

    #  从页面post数据中获取用户并赋值给yinshilog的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        yinshilog.user = userstr;

    #  从页面post数据中获取用户id并赋值给yinshilog的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        yinshilog.userid = useridstr;

    #  调用save方法保存饮食记录信息
    yinshilog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改饮食记录成功,并跳转到饮食记录管理页面
    return HttpResponse(u"<p>修改饮食记录成功</p><a href='/yinshilog/useryinshilogmanage'>返回页面</a>");


#  定义user删除饮食记录信息
def userdeleteyinshilogact(request, id):
    #  根据页面传入的饮食记录id信息，删除出对应的饮食记录信息
    models.Yinshilog.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除饮食记录成功，并跳转到饮食记录管理页面
    return HttpResponse(u"<p>删除饮食记录成功</p><a href='/yinshilog/useryinshilogmanage'>返回页面</a>");


#  处理添加饮食记录Json方法
def addyinshilogactjson(request):
    result = {};
    # 从request中获取内容信息
    name = getQuery(request, "name");
    # 从request中获取卡路里信息
    kaluli = getQuery(request, "kaluli");
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");

    #  将饮食记录的属性赋值给饮食记录，生成饮食记录对象
    yinshilog = models.Yinshilog(name=name, kaluli=kaluli, shijian=shijian, user=user, userid=userid, );

    #  调用save方法保存饮食记录信息
    yinshilog.save();
    result['message'] = "添加饮食记录成功"
    result['code'] = "202"

    #  返回添加饮食记录的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改饮食记录方法   
def updateyinshilogactjson(request):
    result = {};

    #  使用request获取post中的饮食记录id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的饮食记录id获取对应的饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);
    # 从request中获取内容信息
    name = getQuery(request, "name");
    # 如果request中存在内容信息，赋值给饮食记录
    if (name != ""):
        yinshilog.name = name;
    # 从request中获取卡路里信息
    kaluli = getQuery(request, "kaluli");
    # 如果request中存在卡路里信息，赋值给饮食记录
    if (kaluli != ""):
        yinshilog.kaluli = kaluli;
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 如果request中存在时间信息，赋值给饮食记录
    if (shijian != ""):
        yinshilog.shijian = shijian;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给饮食记录
    if (user != ""):
        yinshilog.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给饮食记录
    if (userid != ""):
        yinshilog.userid = userid;

    #  调用save方法保存饮食记录信息
    yinshilog.save();
    result['message'] = "修改饮食记录成功"
    result['code'] = "202"

    #  返回修改饮食记录的结果
    return HttpResponse(json.dumps(result));


#  定义删除饮食记录方法   
def deleteyinshilogjson(request):
    result = {};

    #  使用request获取post中的饮食记录id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除饮食记录信息
    models.Yinshilog.objects.filter(id=id).delete();
    result['message'] = "删除饮食记录成功"
    result['code'] = "202"

    #  返回删除饮食记录的结果
    return HttpResponse(json.dumps(result));


#  定义搜索饮食记录json方法，响应页面搜索请求   
def searchyinshilogjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的饮食记录信息
    yinshilogall = models.Yinshilog.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的饮食记录信息
    result['yinshilogall'] = objtodic(yinshilogall)
    result['message'] = "查询饮食记录成功"
    result['code'] = "202"

    #  返回查询饮食记录的结果
    return HttpResponse(json.dumps(result));


#  处理饮食记录详情   
def yinshilogdetailsjson(request):
    result = {};

    #  使用request获取post中的饮食记录id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取饮食记录信息
    yinshilog = models.Yinshilog.objects.get(id=id);
    result['yinshilog'] = objtodic(yinshilog);
    result['message'] = "查询饮食记录成功"
    result['code'] = "202"

    #  返回查询饮食记录详情的结果
    return HttpResponse(json.dumps(result));
