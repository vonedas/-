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


#    定义添加锻炼记录的方法，响应页面请求
def addduanlianlog(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加锻炼记录页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addduanlianlog.html', {'userall': userall, });


#  处理添加锻炼记录方法   
def addduanlianlogact(request):
    #  从页面post数据中获取项目
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取卡路里（千卡）
    kalulistr = request.POST.get("kaluli");
    kaluli = "";
    if (kalulistr is not None):
        kaluli = kalulistr;

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

    #  将锻炼记录的属性赋值给锻炼记录，生成锻炼记录对象
    duanlianlog = models.Duanlianlog(name=name, kaluli=kaluli, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存锻炼记录信息
    duanlianlog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加锻炼记录成功,并跳转到锻炼记录管理页面
    return HttpResponse(u"<p>添加锻炼记录成功</p><a href='/duanlianlog/duanlianlogmanage'>返回页面</a>");


#  定义表名管理方法，响应页面duanlianlogmanage请求   
def duanlianlogmanage(request):
    #  通过all方法查询所有的锻炼记录信息
    duanlianlogall = models.Duanlianlog.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到锻炼记录管理页面，并附带所有锻炼记录信息
    return render(request, 'xitong/duanlianlogmanage.html', {'duanlianlogall': duanlianlogall});


#  定义表名查看方法，响应页面duanlianlogview请求   
def duanlianlogview(request):
    #  通过all方法查询所有的锻炼记录信息
    duanlianlogall = models.Duanlianlog.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到锻炼记录查看页面，并附带所有锻炼记录信息
    return render(request, 'xitong/duanlianlogview.html', {'duanlianlogall': duanlianlogall});


#  定义修改锻炼记录方法，通过id查询对应的锻炼记录信息，返回页面展示  
def updateduanlianlog(request, id):
    #  使用get方法，通过id查询对应的锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改锻炼记录页面，并附带当前锻炼记录信息
    return render(request, 'xitong/updateduanlianlog.html', {'duanlianlog': duanlianlog, 'userall': userall, });


#  定义处理修改锻炼记录方法   
def updateduanlianlogact(request):
    #  使用request获取post中的锻炼记录id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的锻炼记录id获取对应的锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);

    #  从页面post数据中获取项目并赋值给duanlianlog的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        duanlianlog.name = namestr;

    #  从页面post数据中获取卡路里（千卡）并赋值给duanlianlog的kaluli字段
    kalulistr = request.POST.get("kaluli");
    if (kalulistr is not None):
        duanlianlog.kaluli = kalulistr;

    #  从页面post数据中获取用户并赋值给duanlianlog的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        duanlianlog.user = userstr;

    #  从页面post数据中获取用户id并赋值给duanlianlog的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        duanlianlog.userid = useridstr;

    #  从页面post数据中获取时间并赋值给duanlianlog的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        duanlianlog.shijian = shijianstr;

    #  调用save方法保存锻炼记录信息
    duanlianlog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改锻炼记录成功,并跳转到锻炼记录管理页面
    return HttpResponse(u"<p>修改锻炼记录成功</p><a href='/duanlianlog/duanlianlogmanage'>返回页面</a>");


#  定义删除锻炼记录方法   
def deleteduanlianlogact(request, id):
    #  调用django的delete方法，根据id删除锻炼记录信息
    models.Duanlianlog.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除锻炼记录成功,并跳转到锻炼记录管理页面
    return HttpResponse(u"<p>删除锻炼记录成功</p><a href='/duanlianlog/duanlianlogmanage'>返回页面</a>");


#  定义搜索锻炼记录方法，响应页面搜索请求   
def searchduanlianlog(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的锻炼记录信息
    duanlianlogall = models.Duanlianlog.objects.filter(name__icontains=search);

    #  跳转到搜索锻炼记录页面，并附带查询的锻炼记录信息
    return render(request, 'xitong/searchduanlianlog.html', {"duanlianlogall": duanlianlogall});


#  处理锻炼记录详情   
def duanlianlogdetails(request, id):
    #  根据页面传入id获取锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到锻炼记录详情页面,并锻炼记录信息传递到页面中
    return render(request, 'xitong/duanlianlogdetails.html', {"duanlianlog": duanlianlog});


#  定义跳转user添加锻炼记录页面的方法  
def useraddduanlianlog(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加锻炼记录页面
    return render(request, 'xitong/useraddduanlianlog.html', {'userall': userall, });


#  处理添加锻炼记录方法   
def useraddduanlianlogact(request):
    #  从页面post数据中获取项目
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取卡路里（千卡）
    kalulistr = request.POST.get("kaluli");
    kaluli = "";
    if (kalulistr is not None):
        kaluli = kalulistr;

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

    #  将锻炼记录的属性赋值给锻炼记录，生成锻炼记录对象
    duanlianlog = models.Duanlianlog(name=name, kaluli=kaluli, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存锻炼记录信息
    duanlianlog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加锻炼记录成功,并跳转到锻炼记录管理页面
    return HttpResponse(u"<p>添加锻炼记录成功</p><a href='/duanlianlog/userduanlianlogmanage'>返回页面</a>");


#  跳转user锻炼记录管理页面
def userduanlianlogmanage(request):
    #  查询出userid等于当前用户id的所有锻炼记录信息
    duanlianlogall = models.Duanlianlog.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回锻炼记录管理页面，并携带duanlianlogall的数据信息
    return render(request, 'xitong/userduanlianlogmanage.html', {'duanlianlogall': duanlianlogall});


#  定义跳转user修改锻炼记录页面      
def userupdateduanlianlog(request, id):
    #  根据页面传入的锻炼记录id信息，查询出对应的锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改锻炼记录页面，并携带查询出的锻炼记录信息
    return render(request, 'xitong/userupdateduanlianlog.html', {'duanlianlog': duanlianlog, 'userall': userall, });


#  定义处理修改锻炼记录方法   
def userupdateduanlianlogact(request):
    #  使用request获取post中的锻炼记录id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的锻炼记录id获取对应的锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);

    #  从页面post数据中获取项目并赋值给duanlianlog的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        duanlianlog.name = namestr;

    #  从页面post数据中获取卡路里（千卡）并赋值给duanlianlog的kaluli字段
    kalulistr = request.POST.get("kaluli");
    if (kalulistr is not None):
        duanlianlog.kaluli = kalulistr;

    #  从页面post数据中获取用户并赋值给duanlianlog的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        duanlianlog.user = userstr;

    #  从页面post数据中获取用户id并赋值给duanlianlog的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        duanlianlog.userid = useridstr;

    #  从页面post数据中获取时间并赋值给duanlianlog的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        duanlianlog.shijian = shijianstr;

    #  调用save方法保存锻炼记录信息
    duanlianlog.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改锻炼记录成功,并跳转到锻炼记录管理页面
    return HttpResponse(u"<p>修改锻炼记录成功</p><a href='/duanlianlog/userduanlianlogmanage'>返回页面</a>");


#  定义user删除锻炼记录信息
def userdeleteduanlianlogact(request, id):
    #  根据页面传入的锻炼记录id信息，删除出对应的锻炼记录信息
    models.Duanlianlog.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除锻炼记录成功，并跳转到锻炼记录管理页面
    return HttpResponse(u"<p>删除锻炼记录成功</p><a href='/duanlianlog/userduanlianlogmanage'>返回页面</a>");


#  处理添加锻炼记录Json方法
def addduanlianlogactjson(request):
    result = {};
    # 从request中获取项目信息
    name = getQuery(request, "name");
    # 从request中获取卡路里（千卡）信息
    kaluli = getQuery(request, "kaluli");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");

    #  将锻炼记录的属性赋值给锻炼记录，生成锻炼记录对象
    duanlianlog = models.Duanlianlog(name=name, kaluli=kaluli, user=user, userid=userid, shijian=shijian, );

    #  调用save方法保存锻炼记录信息
    duanlianlog.save();
    result['message'] = "添加锻炼记录成功"
    result['code'] = "202"

    #  返回添加锻炼记录的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改锻炼记录方法   
def updateduanlianlogactjson(request):
    result = {};

    #  使用request获取post中的锻炼记录id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的锻炼记录id获取对应的锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);
    # 从request中获取项目信息
    name = getQuery(request, "name");
    # 如果request中存在项目信息，赋值给锻炼记录
    if (name != ""):
        duanlianlog.name = name;
    # 从request中获取卡路里（千卡）信息
    kaluli = getQuery(request, "kaluli");
    # 如果request中存在卡路里（千卡）信息，赋值给锻炼记录
    if (kaluli != ""):
        duanlianlog.kaluli = kaluli;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给锻炼记录
    if (user != ""):
        duanlianlog.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给锻炼记录
    if (userid != ""):
        duanlianlog.userid = userid;
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 如果request中存在时间信息，赋值给锻炼记录
    if (shijian != ""):
        duanlianlog.shijian = shijian;

    #  调用save方法保存锻炼记录信息
    duanlianlog.save();
    result['message'] = "修改锻炼记录成功"
    result['code'] = "202"

    #  返回修改锻炼记录的结果
    return HttpResponse(json.dumps(result));


#  定义删除锻炼记录方法   
def deleteduanlianlogjson(request):
    result = {};

    #  使用request获取post中的锻炼记录id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除锻炼记录信息
    models.Duanlianlog.objects.filter(id=id).delete();
    result['message'] = "删除锻炼记录成功"
    result['code'] = "202"

    #  返回删除锻炼记录的结果
    return HttpResponse(json.dumps(result));


#  定义搜索锻炼记录json方法，响应页面搜索请求   
def searchduanlianlogjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的锻炼记录信息
    duanlianlogall = models.Duanlianlog.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的锻炼记录信息
    result['duanlianlogall'] = objtodic(duanlianlogall)
    result['message'] = "查询锻炼记录成功"
    result['code'] = "202"

    #  返回查询锻炼记录的结果
    return HttpResponse(json.dumps(result));


#  处理锻炼记录详情   
def duanlianlogdetailsjson(request):
    result = {};

    #  使用request获取post中的锻炼记录id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取锻炼记录信息
    duanlianlog = models.Duanlianlog.objects.get(id=id);
    result['duanlianlog'] = objtodic(duanlianlog);
    result['message'] = "查询锻炼记录成功"
    result['code'] = "202"

    #  返回查询锻炼记录详情的结果
    return HttpResponse(json.dumps(result));


# 获取运动类型列表
def getMotionTypes(request):
    result = {};
    # 获取当前用户ID
    userid = getQuery(request, "userid")
    if not userid:
        result['message'] = "用户未登录"
        result['code'] = "401"
        return HttpResponse(json.dumps(result))

    try:
        # 查询系统预设（userid=0）和用户自定义的运动类型
        motiontypes = models.Motiontype.objects.filter(userid__in=[0, int(userid)])
        result['motiontypes'] = objtodic(motiontypes)
        result['message'] = "获取运动类型成功"
        result['code'] = "200"
    except Exception as e:
        result['message'] = "获取运动类型失败：" + str(e)
        result['code'] = "500"

    return HttpResponse(json.dumps(result))


# 计算卡路里
def calculateCalories(request):
    result = {};
    # 获取参数
    motiontype_id = getQuery(request, "motiontype_id")
    duration = getQuery(request, "duration")  # 运动时长（分钟）

    try:
        # 获取运动类型
        motiontype = models.Motiontype.objects.get(id=motiontype_id)
        # 计算卡路里 = 运动强度 * 时长
        calories = float(motiontype.value) * float(duration)
        result['calories'] = round(calories, 2)
        result['message'] = "计算卡路里成功"
        result['code'] = "200"
    except Exception as e:
        result['message'] = "计算卡路里失败：" + str(e)
        result['code'] = "500"

    return HttpResponse(json.dumps(result))
