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


#    定义添加饮食剩余的方法，响应页面请求
def addyinshi(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加饮食剩余页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addyinshi.html', {'userall': userall, });


#  处理添加饮食剩余方法   
def addyinshiact(request):
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

    #  从页面post数据中获取剩余
    shengyustr = request.POST.get("shengyu");
    shengyu = "";
    if (shengyustr is not None):
        shengyu = shengyustr;

    #  从页面post数据中获取日期
    riqistr = request.POST.get("riqi");
    riqi = "";
    if (riqistr is not None):
        riqi = riqistr;

    #  将饮食剩余的属性赋值给饮食剩余，生成饮食剩余对象
    yinshi = models.Yinshi(user=user, userid=userid, shengyu=shengyu, riqi=riqi, );

    #  调用save方法保存饮食剩余信息
    yinshi.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加饮食剩余成功,并跳转到饮食剩余管理页面
    return HttpResponse(u"<p>添加饮食剩余成功</p><a href='/yinshi/yinshimanage'>返回页面</a>");


#  定义表名管理方法，响应页面yinshimanage请求   
def yinshimanage(request):
    #  通过all方法查询所有的饮食剩余信息
    yinshiall = models.Yinshi.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到饮食剩余管理页面，并附带所有饮食剩余信息
    return render(request, 'xitong/yinshimanage.html', {'yinshiall': yinshiall});


#  定义表名查看方法，响应页面yinshiview请求   
def yinshiview(request):
    #  通过all方法查询所有的饮食剩余信息
    yinshiall = models.Yinshi.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到饮食剩余查看页面，并附带所有饮食剩余信息
    return render(request, 'xitong/yinshiview.html', {'yinshiall': yinshiall});


#  定义修改饮食剩余方法，通过id查询对应的饮食剩余信息，返回页面展示  
def updateyinshi(request, id):
    #  使用get方法，通过id查询对应的饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改饮食剩余页面，并附带当前饮食剩余信息
    return render(request, 'xitong/updateyinshi.html', {'yinshi': yinshi, 'userall': userall, });


#  定义处理修改饮食剩余方法   
def updateyinshiact(request):
    #  使用request获取post中的饮食剩余id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的饮食剩余id获取对应的饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给yinshi的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        yinshi.user = userstr;

    #  从页面post数据中获取用户id并赋值给yinshi的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        yinshi.userid = useridstr;

    #  从页面post数据中获取剩余并赋值给yinshi的shengyu字段
    shengyustr = request.POST.get("shengyu");
    if (shengyustr is not None):
        yinshi.shengyu = shengyustr;

    #  从页面post数据中获取日期并赋值给yinshi的riqi字段
    riqistr = request.POST.get("riqi");
    if (riqistr is not None):
        yinshi.riqi = riqistr;

    #  调用save方法保存饮食剩余信息
    yinshi.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改饮食剩余成功,并跳转到饮食剩余管理页面
    return HttpResponse(u"<p>修改饮食剩余成功</p><a href='/yinshi/yinshimanage'>返回页面</a>");


#  定义删除饮食剩余方法   
def deleteyinshiact(request, id):
    #  调用django的delete方法，根据id删除饮食剩余信息
    models.Yinshi.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除饮食剩余成功,并跳转到饮食剩余管理页面
    return HttpResponse(u"<p>删除饮食剩余成功</p><a href='/yinshi/yinshimanage'>返回页面</a>");


#  定义搜索饮食剩余方法，响应页面搜索请求   
def searchyinshi(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的饮食剩余信息
    yinshiall = models.Yinshi.objects.filter(user__icontains=search);

    #  跳转到搜索饮食剩余页面，并附带查询的饮食剩余信息
    return render(request, 'xitong/searchyinshi.html', {"yinshiall": yinshiall});


#  处理饮食剩余详情   
def yinshidetails(request, id):
    #  根据页面传入id获取饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到饮食剩余详情页面,并饮食剩余信息传递到页面中
    return render(request, 'xitong/yinshidetails.html', {"yinshi": yinshi});


#  定义跳转user添加饮食剩余页面的方法  
def useraddyinshi(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加饮食剩余页面
    return render(request, 'xitong/useraddyinshi.html', {'userall': userall, });


#  处理添加饮食剩余方法   
def useraddyinshiact(request):
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

    #  从页面post数据中获取剩余
    shengyustr = request.POST.get("shengyu");
    shengyu = "";
    if (shengyustr is not None):
        shengyu = shengyustr;

    #  从页面post数据中获取日期
    riqistr = request.POST.get("riqi");
    riqi = "";
    if (riqistr is not None):
        riqi = riqistr;

    #  将饮食剩余的属性赋值给饮食剩余，生成饮食剩余对象
    yinshi = models.Yinshi(user=user, userid=userid, shengyu=shengyu, riqi=riqi, );

    #  调用save方法保存饮食剩余信息
    yinshi.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加饮食剩余成功,并跳转到饮食剩余管理页面
    return HttpResponse(u"<p>添加饮食剩余成功</p><a href='/yinshi/useryinshimanage'>返回页面</a>");


#  跳转user饮食剩余管理页面
def useryinshimanage(request):
    #  查询出userid等于当前用户id的所有饮食剩余信息
    yinshiall = models.Yinshi.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回饮食剩余管理页面，并携带yinshiall的数据信息
    return render(request, 'xitong/useryinshimanage.html', {'yinshiall': yinshiall});


#  定义跳转user修改饮食剩余页面      
def userupdateyinshi(request, id):
    #  根据页面传入的饮食剩余id信息，查询出对应的饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改饮食剩余页面，并携带查询出的饮食剩余信息
    return render(request, 'xitong/userupdateyinshi.html', {'yinshi': yinshi, 'userall': userall, });


#  定义处理修改饮食剩余方法   
def userupdateyinshiact(request):
    #  使用request获取post中的饮食剩余id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的饮食剩余id获取对应的饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给yinshi的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        yinshi.user = userstr;

    #  从页面post数据中获取用户id并赋值给yinshi的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        yinshi.userid = useridstr;

    #  从页面post数据中获取剩余并赋值给yinshi的shengyu字段
    shengyustr = request.POST.get("shengyu");
    if (shengyustr is not None):
        yinshi.shengyu = shengyustr;

    #  从页面post数据中获取日期并赋值给yinshi的riqi字段
    riqistr = request.POST.get("riqi");
    if (riqistr is not None):
        yinshi.riqi = riqistr;

    #  调用save方法保存饮食剩余信息
    yinshi.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改饮食剩余成功,并跳转到饮食剩余管理页面
    return HttpResponse(u"<p>修改饮食剩余成功</p><a href='/yinshi/useryinshimanage'>返回页面</a>");


#  定义user删除饮食剩余信息
def userdeleteyinshiact(request, id):
    #  根据页面传入的饮食剩余id信息，删除出对应的饮食剩余信息
    models.Yinshi.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除饮食剩余成功，并跳转到饮食剩余管理页面
    return HttpResponse(u"<p>删除饮食剩余成功</p><a href='/yinshi/useryinshimanage'>返回页面</a>");


#  处理添加饮食剩余Json方法
def addyinshiactjson(request):
    result = {};
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取剩余信息
    shengyu = getQuery(request, "shengyu");
    # 从request中获取日期信息
    riqi = getQuery(request, "riqi");

    #  将饮食剩余的属性赋值给饮食剩余，生成饮食剩余对象
    yinshi = models.Yinshi(user=user, userid=userid, shengyu=shengyu, riqi=riqi, );

    #  调用save方法保存饮食剩余信息
    yinshi.save();
    result['message'] = "添加饮食剩余成功"
    result['code'] = "202"

    #  返回添加饮食剩余的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改饮食剩余方法   
def updateyinshiactjson(request):
    result = {};

    #  使用request获取post中的饮食剩余id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的饮食剩余id获取对应的饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给饮食剩余
    if (user != ""):
        yinshi.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给饮食剩余
    if (userid != ""):
        yinshi.userid = userid;
    # 从request中获取剩余信息
    shengyu = getQuery(request, "shengyu");
    # 如果request中存在剩余信息，赋值给饮食剩余
    if (shengyu != ""):
        yinshi.shengyu = shengyu;
    # 从request中获取日期信息
    riqi = getQuery(request, "riqi");
    # 如果request中存在日期信息，赋值给饮食剩余
    if (riqi != ""):
        yinshi.riqi = riqi;

    #  调用save方法保存饮食剩余信息
    yinshi.save();
    result['message'] = "修改饮食剩余成功"
    result['code'] = "202"

    #  返回修改饮食剩余的结果
    return HttpResponse(json.dumps(result));


#  定义删除饮食剩余方法   
def deleteyinshijson(request):
    result = {};

    #  使用request获取post中的饮食剩余id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除饮食剩余信息
    models.Yinshi.objects.filter(id=id).delete();
    result['message'] = "删除饮食剩余成功"
    result['code'] = "202"

    #  返回删除饮食剩余的结果
    return HttpResponse(json.dumps(result));


#  定义搜索饮食剩余json方法，响应页面搜索请求   
def searchyinshijson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的饮食剩余信息
    yinshiall = models.Yinshi.objects.filter(user__icontains=search);

    #  返回查询结果，附带查询的饮食剩余信息
    result['yinshiall'] = objtodic(yinshiall)
    result['message'] = "查询饮食剩余成功"
    result['code'] = "202"

    #  返回查询饮食剩余的结果
    return HttpResponse(json.dumps(result));


#  处理饮食剩余详情   
def yinshidetailsjson(request):
    result = {};

    #  使用request获取post中的饮食剩余id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取饮食剩余信息
    yinshi = models.Yinshi.objects.get(id=id);
    result['yinshi'] = objtodic(yinshi);
    result['message'] = "查询饮食剩余成功"
    result['code'] = "202"

    #  返回查询饮食剩余详情的结果
    return HttpResponse(json.dumps(result));
