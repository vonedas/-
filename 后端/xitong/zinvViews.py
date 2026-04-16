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


#    定义添加子女的方法，响应页面请求
def addzinv(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加子女页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addzinv.html', {});


#  处理添加子女方法   
def addzinvact(request):
    #  从页面post数据中获取名字
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

    #  从页面post数据中获取性别
    sexstr = request.POST.get("sex");
    sex = "";
    if (sexstr is not None):
        sex = sexstr;

    #  从页面post数据中获取电话
    telstr = request.POST.get("tel");
    tel = "";
    if (telstr is not None):
        tel = telstr;

    #  从页面post数据中获取头像
    picstr = request.POST.get("pic");
    pic = "";
    if (picstr is not None):
        pic = picstr;

    #  将子女的属性赋值给子女，生成子女对象
    zinv = models.Zinv(name=name, username=username, password=password, sex=sex, tel=tel, pic=pic, );

    #  调用save方法保存子女信息
    zinv.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加子女成功,并跳转到子女管理页面
    return HttpResponse(u"<p>添加子女成功</p><a href='/zinv/zinvmanage'>返回页面</a>");


#  定义表名管理方法，响应页面zinvmanage请求   
def zinvmanage(request):
    #  通过all方法查询所有的子女信息
    zinvall = models.Zinv.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到子女管理页面，并附带所有子女信息
    return render(request, 'xitong/zinvmanage.html', {'zinvall': zinvall});


#  定义表名查看方法，响应页面zinvview请求   
def zinvview(request):
    #  通过all方法查询所有的子女信息
    zinvall = models.Zinv.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到子女查看页面，并附带所有子女信息
    return render(request, 'xitong/zinvview.html', {'zinvall': zinvall});


#  定义修改子女方法，通过id查询对应的子女信息，返回页面展示  
def updatezinv(request, id):
    #  使用get方法，通过id查询对应的子女信息
    zinv = models.Zinv.objects.get(id=id);

    #  跳转到修改子女页面，并附带当前子女信息
    return render(request, 'xitong/updatezinv.html', {'zinv': zinv, });


#  定义处理修改子女方法   
def updatezinvact(request):
    #  使用request获取post中的子女id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的子女id获取对应的子女信息
    zinv = models.Zinv.objects.get(id=id);

    #  从页面post数据中获取名字并赋值给zinv的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        zinv.name = namestr;

    #  从页面post数据中获取账号并赋值给zinv的username字段
    usernamestr = request.POST.get("username");
    if (usernamestr is not None):
        zinv.username = usernamestr;

    #  从页面post数据中获取密码并赋值给zinv的password字段
    passwordstr = request.POST.get("password");
    if (passwordstr is not None):
        zinv.password = passwordstr;

    #  从页面post数据中获取性别并赋值给zinv的sex字段
    sexstr = request.POST.get("sex");
    if (sexstr is not None):
        zinv.sex = sexstr;

    #  从页面post数据中获取电话并赋值给zinv的tel字段
    telstr = request.POST.get("tel");
    if (telstr is not None):
        zinv.tel = telstr;

    #  从页面post数据中获取头像并赋值给zinv的pic字段
    picstr = request.POST.get("pic");
    if (picstr is not None):
        zinv.pic = picstr;

    #  调用save方法保存子女信息
    zinv.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改子女成功,并跳转到子女管理页面
    return HttpResponse(u"<p>修改子女成功</p><a href='/zinv/zinvmanage'>返回页面</a>");


#  定义删除子女方法   
def deletezinvact(request, id):
    #  调用django的delete方法，根据id删除子女信息
    models.Zinv.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除子女成功,并跳转到子女管理页面
    return HttpResponse(u"<p>删除子女成功</p><a href='/zinv/zinvmanage'>返回页面</a>");


#  定义搜索子女方法，响应页面搜索请求   
def searchzinv(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的子女信息
    zinvall = models.Zinv.objects.filter(name__icontains=search);

    #  跳转到搜索子女页面，并附带查询的子女信息
    return render(request, 'xitong/searchzinv.html', {"zinvall": zinvall});


#  处理子女详情   
def zinvdetails(request, id):
    #  根据页面传入id获取子女信息
    zinv = models.Zinv.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到子女详情页面,并子女信息传递到页面中
    return render(request, 'xitong/zinvdetails.html', {"zinv": zinv});


#  处理添加子女Json方法
def addzinvactjson(request):
    result = {};
    # 从request中获取名字信息
    name = getQuery(request, "name");
    # 从request中获取账号信息
    username = getQuery(request, "username");
    # 从request中获取密码信息
    password = getQuery(request, "password");
    # 从request中获取性别信息
    sex = getQuery(request, "sex");
    # 从request中获取电话信息
    tel = getQuery(request, "tel");
    # 从request中获取头像信息
    pic = getQuery(request, "pic");

    #  将子女的属性赋值给子女，生成子女对象
    zinv = models.Zinv(name=name, username=username, password=password, sex=sex, tel=tel, pic=pic, );

    #  调用save方法保存子女信息
    zinv.save();
    result['message'] = "添加子女成功"
    result['code'] = "202"

    #  返回添加子女的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改子女方法   
def updatezinvactjson(request):
    result = {};

    #  使用request获取post中的子女id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的子女id获取对应的子女信息
    zinv = models.Zinv.objects.get(id=id);
    # 从request中获取名字信息
    name = getQuery(request, "name");
    # 如果request中存在名字信息，赋值给子女
    if (name != ""):
        zinv.name = name;
    # 从request中获取账号信息
    username = getQuery(request, "username");
    # 如果request中存在账号信息，赋值给子女
    if (username != ""):
        zinv.username = username;
    # 从request中获取密码信息
    password = getQuery(request, "password");
    # 如果request中存在密码信息，赋值给子女
    if (password != ""):
        zinv.password = password;
    # 从request中获取性别信息
    sex = getQuery(request, "sex");
    # 如果request中存在性别信息，赋值给子女
    if (sex != ""):
        zinv.sex = sex;
    # 从request中获取电话信息
    tel = getQuery(request, "tel");
    # 如果request中存在电话信息，赋值给子女
    if (tel != ""):
        zinv.tel = tel;
    # 从request中获取头像信息
    pic = getQuery(request, "pic");
    # 如果request中存在头像信息，赋值给子女
    if (pic != ""):
        zinv.pic = pic;

    #  调用save方法保存子女信息
    zinv.save();
    result['message'] = "修改子女成功"
    result['code'] = "202"

    #  返回修改子女的结果
    return HttpResponse(json.dumps(result));


#  定义删除子女方法   
def deletezinvjson(request):
    result = {};

    #  使用request获取post中的子女id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除子女信息
    models.Zinv.objects.filter(id=id).delete();
    result['message'] = "删除子女成功"
    result['code'] = "202"

    #  返回删除子女的结果
    return HttpResponse(json.dumps(result));


#  定义搜索子女json方法，响应页面搜索请求   
def searchzinvjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的子女信息
    zinvall = models.Zinv.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的子女信息
    result['zinvall'] = objtodic(zinvall)
    result['message'] = "查询子女成功"
    result['code'] = "202"

    #  返回查询子女的结果
    return HttpResponse(json.dumps(result));


#  处理子女详情   
def zinvdetailsjson(request):
    result = {};

    #  使用request获取post中的子女id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取子女信息
    zinv = models.Zinv.objects.get(id=id);
    result['zinv'] = objtodic(zinv);
    result['message'] = "查询子女成功"
    result['code'] = "202"

    #  返回查询子女详情的结果
    return HttpResponse(json.dumps(result));
