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
import datetime


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


#    定义添加用户的方法，响应页面请求
def adduser(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加用户页面，并将该页面数据传递到视图中
    return render(request, 'xitong/adduser.html', {});


#  处理添加用户方法
def adduseract(request):
    #  从页面post数据中获取名称
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

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

    #  调用uploadFile方法上传页面中图片
    pic = uploadFile(request, "picfile");

    #  从页面post数据中获取性别
    genderstr = request.POST.get("gender");
    gender = "";
    if (genderstr is not None):
        gender = genderstr;

    #  从页面post数据中获取年龄
    agestr = request.POST.get("age");
    age = "";
    if (agestr is not None):
        age = agestr;

    #  从页面post数据中获取身高
    shengaostr = request.POST.get("shengao");
    shengao = "";
    if (shengaostr is not None):
        shengao = shengaostr;

    #  从页面post数据中获取体重
    tizhongstr = request.POST.get("tizhong");
    tizhong = "";
    if (tizhongstr is not None):
        tizhong = tizhongstr;

    #  从页面post数据中获取电话
    telstr = request.POST.get("tel");
    tel = "";
    if (telstr is not None):
        tel = telstr;

    #  从页面post数据中获取锻炼消耗
    duanlianstr = request.POST.get("duanlian");
    duanlian = "";
    if (duanlianstr is not None):
        duanlian = duanlianstr;

    #  从页面post数据中获取需求卡路里
    xuqiustr = request.POST.get("xuqiu");
    xuqiu = "";
    if (xuqiustr is not None):
        xuqiu = xuqiustr;

    statusstr = request.POST.get("status");
    status = "";
    if (statusstr is not None):
        status = statusstr;
    #  将用户的属性赋值给用户，生成用户对象
    user = models.User(name=name, username=username, password=password, pic=pic, gender=gender, age=age,
                       shengao=shengao, tizhong=tizhong, tel=tel, duanlian=duanlian, xuqiu=xuqiu, status=status,);

    #  调用save方法保存用户信息
    user.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加用户成功,并跳转到用户管理页面
    return HttpResponse(u"<p>添加用户成功</p><a href='/user/usermanage'>返回页面</a>");


#  定义表名管理方法，响应页面usermanage请求   
def usermanage(request):
    #  通过all方法查询所有的用户信息
    userall = models.User.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到用户管理页面，并附带所有用户信息
    return render(request, 'xitong/usermanage.html', {'userall': userall});


#  定义表名查看方法，响应页面userview请求   
def userview(request):
    #  通过all方法查询所有的用户信息
    userall = models.User.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到用户查看页面，并附带所有用户信息
    return render(request, 'xitong/userview.html', {'userall': userall});


#  定义修改用户方法，通过id查询对应的用户信息，返回页面展示  
def updateuser(request, id):
    #  使用get方法，通过id查询对应的用户信息
    user = models.User.objects.get(id=id);

    #  跳转到修改用户页面，并附带当前用户信息
    return render(request, 'xitong/updateuser.html', {'user': user, });


#  定义处理修改用户方法   
def updateuseract(request):
    #  使用request获取post中的用户id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的用户id获取对应的用户信息
    user = models.User.objects.get(id=id);

    #  从页面post数据中获取名称并赋值给user的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        user.name = namestr;

    #  从页面post数据中获取账号并赋值给user的username字段
    usernamestr = request.POST.get("username");
    if (usernamestr is not None):
        user.username = usernamestr;

    #  从页面post数据中获取密码并赋值给user的password字段
    passwordstr = request.POST.get("password");
    if (passwordstr is not None):
        user.password = passwordstr;

    #  调用uploadFile方法上传页面中图片
    picfile = uploadFile(request, "picfile");

    #  如果picfile不等于false
    if (picfile != "false"):
        #  将picfile赋值给用户的图片字段
        user.pic = picfile;

    #  从页面post数据中获取性别并赋值给user的gender字段
    genderstr = request.POST.get("gender");
    if (genderstr is not None):
        user.gender = genderstr;

    #  从页面post数据中获取年龄并赋值给user的age字段
    agestr = request.POST.get("age");
    if (agestr is not None):
        user.age = agestr;

    #  从页面post数据中获取身高并赋值给user的shengao字段
    shengaostr = request.POST.get("shengao");
    if (shengaostr is not None):
        user.shengao = shengaostr;

    #  从页面post数据中获取体重并赋值给user的tizhong字段
    tizhongstr = request.POST.get("tizhong");
    if (tizhongstr is not None):
        user.tizhong = tizhongstr;

    #  从页面post数据中获取电话并赋值给user的tel字段
    telstr = request.POST.get("tel");
    if (telstr is not None):
        user.tel = telstr;

    #  从页面post数据中获取锻炼消耗并赋值给user的duanlian字段
    duanlianstr = request.POST.get("duanlian");
    if (duanlianstr is not None):
        user.duanlian = duanlianstr;

    #  从页面post数据中获取需求卡路里并赋值给user的xuqiu字段
    xuqiustr = request.POST.get("xuqiu");
    if (xuqiustr is not None):
        user.xuqiu = xuqiustr;

    #  调用save方法保存用户信息
    user.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改用户成功,并跳转到用户管理页面
    return HttpResponse(u"<p>修改用户成功</p><a href='/user/usermanage'>返回页面</a>");


#  定义删除用户方法   
def deleteuseract(request, id):
    #  调用django的delete方法，根据id删除用户信息
    models.User.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除用户成功,并跳转到用户管理页面
    return HttpResponse(u"<p>删除用户成功</p><a href='/user/usermanage'>返回页面</a>");


#  定义搜索用户方法，响应页面搜索请求   
def searchuser(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的用户信息
    userall = models.User.objects.filter(name__icontains=search);

    #  跳转到搜索用户页面，并附带查询的用户信息
    return render(request, 'xitong/searchuser.html', {"userall": userall});


#  处理用户详情   
def userdetails(request, id):
    #  根据页面传入id获取用户信息
    user = models.User.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到用户详情页面,并用户信息传递到页面中
    return render(request, 'xitong/userdetails.html', {"user": user});


#  处理添加用户Json方法
def adduseractjson(request):
    result = {};
    # 从request中获取名称信息
    name = getQuery(request, "name");
    # 从request中获取账号信息
    username = getQuery(request, "username");
    # 从request中获取密码信息
    password = getQuery(request, "password");
    # 从request中获取图片信息
    pic = getQuery(request, "pic");
    # 从request中获取性别信息
    gender = getQuery(request, "gender");
    # 从request中获取年龄信息
    age = getQuery(request, "age");
    # 从request中获取身高信息
    shengao = getQuery(request, "shengao");
    # 从request中获取体重信息
    tizhong = getQuery(request, "tizhong");
    # 从request中获取电话信息
    tel = getQuery(request, "tel");
    # 从request中获取锻炼消耗信息
    duanlian = getQuery(request, "duanlian");
    # 从request中获取需求卡路里信息
    xuqiu = getQuery(request, "xuqiu");

    #  将用户的属性赋值给用户，生成用户对象
    user = models.User(name=name, username=username, password=password, pic=pic, gender=gender, age=age,
                       shengao=shengao, tizhong=tizhong, tel=tel, duanlian=duanlian, xuqiu=xuqiu, );

    #  调用save方法保存用户信息
    user.save();
    result['message'] = "添加用户成功"
    result['code'] = "202"

    #  返回添加用户的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改用户方法   
def updateuseractjson(request):
    result = {};

    #  使用request获取post中的用户id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的用户id获取对应的用户信息
    user = models.User.objects.get(id=id);
    # 从request中获取名称信息
    name = getQuery(request, "name");
    if name not in (None, ""):
        user.name = name
    username = getQuery(request, "username");
    if username not in (None, ""):
        user.username = username
    password = getQuery(request, "password");
    if password not in (None, ""):
        user.password = password
    pic = getQuery(request, "pic");
    if pic not in (None, ""):
        user.pic = pic
    gender = getQuery(request, "gender");
    if gender not in (None, ""):
        user.gender = gender
    age = getQuery(request, "age");
    if age not in (None, ""):
        user.age = age
    shengao = getQuery(request, "shengao");
    if shengao not in (None, ""):
        user.shengao = shengao
    tizhong = getQuery(request, "tizhong");
    if tizhong not in (None, ""):
        user.tizhong = tizhong
    tel = getQuery(request, "tel");
    if tel not in (None, ""):
        user.tel = tel
    duanlian = getQuery(request, "duanlian");
    if duanlian not in (None, ""):
        user.duanlian = duanlian
    xuqiu = getQuery(request, "xuqiu");
    if xuqiu not in (None, ""):
        user.xuqiu = xuqiu

    user.save()
    result['message'] = "修改用户成功"
    result['code'] = "202"
    return HttpResponse(json.dumps(result))


#  定义删除用户方法   
def deleteuserjson(request):
    result = {};

    #  使用request获取post中的用户id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除用户信息
    models.User.objects.filter(id=id).delete();
    result['message'] = "删除用户成功"
    result['code'] = "202"

    #  返回删除用户的结果
    return HttpResponse(json.dumps(result));


#  定义搜索用户json方法，响应页面搜索请求   
def searchuserjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的用户信息
    userall = models.User.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的用户信息
    result['userall'] = objtodic(userall)
    result['message'] = "查询用户成功"
    result['code'] = "202"

    #  返回查询用户的结果
    return HttpResponse(json.dumps(result));

def searchuserjson2(request):
    result = {};

    # 获取页面post参数中的search信息
    search = getQuery(request, "search")
    zinvid = getQuery(request, "zinvid")  # 当前用户id

    # 搜索用户
    userall = models.User.objects.filter(username__icontains=search)

    # 获取当前用户已关注的用户id列表
    followed_ids = []
    if zinvid:
        followed_ids = list(models.Bangding.objects.filter(zinvid=zinvid).values_list('userid', flat=True))

    # 过滤掉已关注的用户
    userall = userall.exclude(id__in=followed_ids)

    result['userall'] = objtodic(userall)
    result['message'] = "查询用户成功"
    result['code'] = "202"
    return HttpResponse(json.dumps(result))

#  处理用户详情   
def userdetailsjson(request):
    result = {};

    #  使用request获取post中的用户id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取用户信息
    user = models.User.objects.get(id=id);
    result['user'] = objtodic(user);
    result['message'] = "查询用户成功"
    result['code'] = "202"

    #  返回查询用户详情的结果
    return HttpResponse(json.dumps(result));

def getmessage(request):
    result = {};
    empty = True

    #  使用request获取post中的用户id参数
    userid = getQuery(request, "userid");

    #  使用django的filter方法过滤查询包含search的用户信息
    bindings = models.Bangding.objects.filter(userid=userid, status=0)
    messages = []
    for bind in bindings:
        user = models.User.objects.get(id=bind.zinvid)
        messages.append({'type':'ask', 'id': bind.id, 'name': user.name})
        empty = False
        break

    if empty:
        today = datetime.datetime.today()
        time = today.strftime('%H:%M')
        date = today.strftime('%Y-%m-%d')
        yao = models.Yao.objects.filter(userid=userid, shijian=time).exclude(date=date)
        for y in yao:
            messages.append({'type':'yao', 'id': y.id, 'name': y.name})
            empty = False
            break

    #  返回查询结果，附带查询的用户信息
    result['message'] = messages
    result['code'] = "200"

    #  返回查询用户的结果
    return HttpResponse(json.dumps(result));

def attention(request):
    result = {};

    #  使用request获取post中的用户id参数
    aid = getQuery(request, "id");
    status = getQuery(request, "status");

    #  使用django的filter方法过滤查询包含search的用户信息
    binding = models.Bangding.objects.get(id=aid)
    binding.status = status
    binding.save()

    #  返回查询结果，附带查询的用户信息
    result['code'] = "200"

    #  返回查询用户的结果
    return HttpResponse(json.dumps(result));

def yao(request):
    result = {};

    #  使用request获取post中的用户id参数
    yid = getQuery(request, "id");

    #  使用django的filter方法过滤查询包含search的用户信息
    yao = models.Yao.objects.get(id=yid)
    today = datetime.datetime.today()
    yao.date = today.strftime('%Y-%m-%d')
    yao.save()

    #  返回查询结果，附带查询的用户信息
    result['code'] = "200"

    #  返回查询用户的结果
    return HttpResponse(json.dumps(result));

def getauth(request):
    result = {};

    #  使用request获取post中的用户参数
    userid = getQuery(request, "userid");
    authid = getQuery(request, "authid");

    #  使用django的filter方法过滤查询包含search的用户信息
    auth = models.Auth.objects.filter(userid=userid, authid=authid)
    res = []
    for a in auth:
        res.append({'id': a.id, 'userid': a.userid, 'authid': a.authid, 'bloodpressure': a.bloodpressure, 'tizhong': a.tizhong, 'xuqiu': a.xuqiu, 'duanlian': a.duanlian, 'diet': a.diet, 'exercise': a.exercise, 'medicine': a.medicine})

    #  返回查询结果，附带查询的用户信息
    result['auth'] = res
    result['code'] = "200"

    #  返回查询用户的结果
    return HttpResponse(json.dumps(result));

def saveauth(request):
    result = {};

    #  使用request获取post中的用户id参数
    aid = getQuery(request, "id");
    userid = getQuery(request, "userid");
    authid = getQuery(request, "authid");
    bloodpressure = getQuery(request, "bloodpressure");
    tizhong = getQuery(request, "tizhong");
    xuqiu = getQuery(request, "xuqiu");
    duanlian = getQuery(request, "duanlian");
    diet = getQuery(request, "diet");
    exercise = getQuery(request, "exercise");
    medicine = getQuery(request, "medicine");

    #  使用django的filter方法过滤查询包含search的用户信息
    auth = models.Auth(id=aid, userid=userid, authid=authid, bloodpressure=bloodpressure, tizhong=tizhong, xuqiu=xuqiu, duanlian=duanlian, diet=diet, exercise=exercise, medicine=medicine)
    auth.save()

    #  返回查询结果，附带查询的用户信息
    result['code'] = "200"

    #  返回查询用户的结果
    return HttpResponse(json.dumps(result));
