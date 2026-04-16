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
import datetime, os, json, random


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


# json上传文件方法
def addfilejson(request):
    # 获取文件源并进行上传
    img = uploadFile(request, "file");

    # 返回保存的文件地址
    return HttpResponse(img);


#  定义跳转到登录页面的方法
def login(request):
    #  返回登录页面
    return render(request, 'xitong/login.html');


#  定义跳转到注册页面的方法
def regist(request):
    #  返回注册页面
    return render(request, 'xitong/regist.html');


#  定义登录方法
def loginact(request):
    #  从POST中获取username
    username = request.POST["username"];

    #  从POST中获取password
    password = request.POST["password"];

    #  从POST中获取identity
    identity = request.POST["identity"];

    #  如果当前登录身份为管理员
    if (identity == '管理员'):

        #  从admin查询是否有账号面与用户输入一直的管理员信息
        admins = models.Admin.objects.filter(username=username, password=password);

        #  如果查询出的数量大于0
        if (admins.count() > 0):
            #  将登录用户的信息保存到session中
            request.session["identity"] = identity;

            #  获取当前登录管理员的id信息
            request.session["id"] = admins[0].id;

            #  获取当前登录管理员的mingzi信息
            request.session["mingzi"] = admins[0].username;

            #  获取登录管理员的管理员id信息，并赋值给session的id字段
            request.session["id"] = admins[0].id;

            #  获取登录管理员的账号信息，并赋值给session的username字段
            request.session["username"] = admins[0].username;

            #  获取登录管理员的密码信息，并赋值给session的password字段
            request.session["password"] = admins[0].password;

            #  跳转到管理员个人中心
            return render(request, 'xitong/adminindex.html');

        #  给出页面提示用户名或密码错误，并跳转到登录页面
        return HttpResponse(u"<p>用户名或密码错误</p><a href='/loginAndRegist/login'>返回页面</a>");

    #  如果当前登录身份为用户
    if (identity == '用户'):

        #  从user查询是否有账号面与用户输入一直的用户信息
        users = models.User.objects.filter(username=username, password=password);

        #  如果查询出的数量大于0
        if (users.count() > 0):
            #  将登录用户的信息保存到session中
            request.session["identity"] = identity;

            #  获取当前登录用户的id信息
            request.session["id"] = users[0].id;

            #  获取当前登录用户的mingzi信息
            request.session["mingzi"] = users[0].name;

            #  获取登录用户的用户id信息，并赋值给session的id字段
            request.session["id"] = users[0].id;

            #  获取登录用户的名称信息，并赋值给session的name字段
            request.session["name"] = users[0].name;

            #  获取登录用户的账号信息，并赋值给session的username字段
            request.session["username"] = users[0].username;

            #  获取登录用户的密码信息，并赋值给session的password字段
            request.session["password"] = users[0].password;

            #  获取登录用户的图片信息，并赋值给session的pic字段
            request.session["pic"] = users[0].pic;

            #  获取登录用户的性别信息，并赋值给session的gender字段
            request.session["gender"] = users[0].gender;

            #  获取登录用户的年龄信息，并赋值给session的age字段
            request.session["age"] = users[0].age;

            #  获取登录用户的身高信息，并赋值给session的shengao字段
            request.session["shengao"] = users[0].shengao;

            #  获取登录用户的体重信息，并赋值给session的tizhong字段
            request.session["tizhong"] = users[0].tizhong;

            #  获取登录用户的电话信息，并赋值给session的tel字段
            request.session["tel"] = users[0].tel;

            #  获取登录用户的锻炼消耗信息，并赋值给session的duanlian字段
            request.session["duanlian"] = users[0].duanlian;

            #  获取登录用户的需求卡路里信息，并赋值给session的xuqiu字段
            request.session["xuqiu"] = users[0].xuqiu;

            #  跳转到用户个人中心
            return render(request, 'xitong/userindex.html');

        #  给出页面提示用户名或密码错误，并跳转到登录页面
        return HttpResponse(u"<p>用户名或密码错误</p><a href='/loginAndRegist/login'>返回页面</a>");

    #  如果当前登录身份为子女
    if (identity == '子女'):

        #  从zinv查询是否有账号面与用户输入一直的子女信息
        zinvs = models.Zinv.objects.filter(username=username, password=password);

        #  如果查询出的数量大于0
        if (zinvs.count() > 0):
            #  将登录用户的信息保存到session中
            request.session["identity"] = identity;

            #  获取当前登录子女的id信息
            request.session["id"] = zinvs[0].id;

            #  获取当前登录子女的mingzi信息
            request.session["mingzi"] = zinvs[0].name;

            #  获取登录子女的子女id信息，并赋值给session的id字段
            request.session["id"] = zinvs[0].id;

            #  获取登录子女的名字信息，并赋值给session的name字段
            request.session["name"] = zinvs[0].name;

            #  获取登录子女的账号信息，并赋值给session的username字段
            request.session["username"] = zinvs[0].username;

            #  获取登录子女的密码信息，并赋值给session的password字段
            request.session["password"] = zinvs[0].password;

            #  获取登录子女的性别信息，并赋值给session的sex字段
            request.session["sex"] = zinvs[0].sex;

            #  获取登录子女的电话信息，并赋值给session的tel字段
            request.session["tel"] = zinvs[0].tel;

            #  获取登录子女的头像信息，并赋值给session的pic字段
            request.session["pic"] = zinvs[0].pic;

            #  跳转到子女个人中心
            return render(request, 'xitong/zinvindex.html');

        #  给出页面提示用户名或密码错误，并跳转到登录页面
        return HttpResponse(u"<p>用户名或密码错误</p><a href='/loginAndRegist/login'>返回页面</a>");

    #  给出页面提示请选择登录身份，并跳转到登录页面
    return HttpResponse(u"<p>请选择登录身份</p><a href='/loginAndRegist/login'>返回页面</a>返回页面</a>");


#  定义登录方法
def loginactjson(request):
    result = {};

    #  从POST中获取username
    username = getQuery(request, "username");

    #  从POST中获取password
    password = getQuery(request, "password");

    #  从POST中获取identity
    identity = getQuery(request, "identity");

    #  如果当前登录身份为管理员
    if (identity == '管理员'):

        #  从admin查询是否有账号面与用户输入一直的管理员信息
        admins = models.Admin.objects.filter(username=username, password=password);

        #  如果查询出的数量大于0
        if (admins.count() > 0):
            #  将登录用户的信息保存到session中
            result["identity"] = identity;

            #  获取当前登录管理员的角色信息
            result["userinfo"] = objtodic(admins[0]);

            #  获取当前登录管理员角色的标识信息
            result["mingzi"] = admins[0].username;

            #  获取当前登录管理员角色的id信息
            result["id"] = admins[0].id;

            #  返回管理员的登录成功信息
            result["message"] = "登录成功";
            return HttpResponse(json.dumps(result));

        #  给出页面提示用户名或密码错误
        result["message"] = "账户或密码错误";
        return HttpResponse(json.dumps(result));

    #  如果当前登录身份为用户
    if (identity == '用户'):

        #  从user查询是否有账号面与用户输入一直的用户信息
        users = models.User.objects.filter(username=username, password=password);

        #  如果查询出的数量大于0
        if (users.count() > 0):
            #  将登录用户的信息保存到session中
            result["identity"] = identity;

            #  获取当前登录用户的角色信息
            result["userinfo"] = objtodic(users[0]);

            #  获取当前登录用户角色的标识信息
            result["mingzi"] = users[0].name;

            #  获取当前登录用户角色的id信息
            result["id"] = users[0].id;

            #  返回用户的登录成功信息
            result["message"] = "登录成功";
            return HttpResponse(json.dumps(result));

        #  给出页面提示用户名或密码错误
        result["message"] = "账户或密码错误";
        return HttpResponse(json.dumps(result));

    #  如果当前登录身份为子女
    if (identity == '子女'):

        #  从zinv查询是否有账号面与用户输入一直的子女信息
        zinvs = models.Zinv.objects.filter(username=username, password=password);

        #  如果查询出的数量大于0
        if (zinvs.count() > 0):
            #  将登录用户的信息保存到session中
            result["identity"] = identity;

            #  获取当前登录子女的角色信息
            result["userinfo"] = objtodic(zinvs[0]);

            #  获取当前登录子女角色的标识信息
            result["mingzi"] = zinvs[0].name;

            #  获取当前登录子女角色的id信息
            result["id"] = zinvs[0].id;

            #  返回子女的登录成功信息
            result["message"] = "登录成功";
            return HttpResponse(json.dumps(result));

        #  给出页面提示用户名或密码错误
        result["message"] = "账户或密码错误";
        return HttpResponse(json.dumps(result));

    #  给出页面提示请选择登录身份
    result["message"] = "请选择登录身份";
    # 返回账号或密码错误信息
    return HttpResponse(json.dumps(result));


#  定义注册方法
def registact(request):
    #  从POST中获取username参数
    username = request.POST["username"];

    #  从POST中获取password参数
    password = request.POST["password"];

    #  从POST中获取identity参数
    identity = request.POST["identity"];

    #  从POST中获取repassword参数
    repassword = request.POST["repassword"];

    #  如果password与repassword不一致
    if (password != repassword):
        #  返回两次密码不一致的提示信息，并返回登录页面
        return HttpResponse(u"<p>两次密码不一致</p><a href='/loginAndRegist/login'>返回页面</a>");

    #  如果当前注册身份为管理员
    if (identity == '管理员'):

        #  根据页面传入的username信息，查询系统中的管理员信息
        admins = models.Admin.objects.filter(username=username);

        #  如果数据数量大于0
        if (admins.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            return HttpResponse(u"<p>该账号已存在</p><a href='/loginAndRegist/regist'>返回页面</a>");
        else:

            #  将传入的管理员信息保存到admin表中
            admin = models.Admin(username=username, password=password);
            admin.save();

            #  给出用户提示注册成功，并跳转到登录页面
            return HttpResponse(u"<p>注册成功</p><a href='/loginAndRegist/login/'>点击跳转到登录界面</a>");

    #  如果当前注册身份为用户
    if (identity == '用户'):

        #  根据页面传入的username信息，查询系统中的用户信息
        users = models.User.objects.filter(username=username);

        #  如果数据数量大于0
        if (users.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            return HttpResponse(u"<p>该账号已存在</p><a href='/loginAndRegist/regist'>返回页面</a>");
        else:

            #  将传入的用户信息保存到user表中
            user = models.User(username=username, password=password);
            user.save();

            #  给出用户提示注册成功，并跳转到登录页面
            return HttpResponse(u"<p>注册成功</p><a href='/loginAndRegist/login/'>点击跳转到登录界面</a>");

    #  如果当前注册身份为子女
    if (identity == '子女'):

        #  根据页面传入的username信息，查询系统中的子女信息
        zinvs = models.Zinv.objects.filter(username=username);

        #  如果数据数量大于0
        if (zinvs.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            return HttpResponse(u"<p>该账号已存在</p><a href='/loginAndRegist/regist'>返回页面</a>");
        else:

            #  将传入的子女信息保存到zinv表中
            zinv = models.Zinv(username=username, password=password);
            zinv.save();

            #  给出用户提示注册成功，并跳转到登录页面
            return HttpResponse(u"<p>注册成功</p><a href='/loginAndRegist/login/'>点击跳转到登录界面</a>");

    #  给出页面提示请选择注册身份，并跳转到注册页面
    return HttpResponse(u"<p>请选择注册身份</p><a href='/loginAndRegist/regist'>返回页面</a>");


#  定义注册方法
def registactjson(request):
    result = {};

    #  从POST中获取username参数
    username = getQuery(request, "username");

    #  从POST中获取password参数
    password = getQuery(request, "password");

    #  从POST中获取identity参数
    identity = getQuery(request, "identity");

    #  从POST中获取repassword参数
    repassword = getQuery(request, "repassword");

    #  如果password与repassword不一致
    if (password != repassword):
        #  返回两次密码不一致的提示信息，并返回登录页面
        result["message"] = "两次密码不一致";
        # 返回账号或密码错误信息
        return HttpResponse(json.dumps(result));

    #  如果当前注册身份为管理员
    if (identity == '管理员'):

        #  根据页面传入的username信息，查询系统中的管理员信息
        admins = models.Admin.objects.filter(username=username);

        #  如果数据数量大于0
        if (admins.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            result["message"] = "该账号已存在";
            return HttpResponse(json.dumps(result));
        else:

            #  将传入的管理员信息保存到admin表中
            admin = models.Admin(username=username, password=password);
            admin.save();

            #  给出用户提示注册成功，并跳转到登录页面
            result["message"] = "注册成功";
            return HttpResponse(json.dumps(result));

    #  如果当前注册身份为用户
    if (identity == '用户'):

        #  根据页面传入的username信息，查询系统中的用户信息
        users = models.User.objects.filter(username=username);

        #  如果数据数量大于0
        if (users.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            result["message"] = "该账号已存在";
            return HttpResponse(json.dumps(result));
        else:

            #  将传入的用户信息保存到user表中
            user = models.User(username=username, password=password);
            user.save();

            #  给出用户提示注册成功，并跳转到登录页面
            result["message"] = "注册成功";
            return HttpResponse(json.dumps(result));

    #  如果当前注册身份为子女
    if (identity == '子女'):

        #  根据页面传入的username信息，查询系统中的子女信息
        zinvs = models.Zinv.objects.filter(username=username);

        #  如果数据数量大于0
        if (zinvs.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            result["message"] = "该账号已存在";
            return HttpResponse(json.dumps(result));
        else:

            #  将传入的子女信息保存到zinv表中
            zinv = models.Zinv(username=username, password=password);
            zinv.save();

            #  给出用户提示注册成功，并跳转到登录页面
            result["message"] = "注册成功";
            return HttpResponse(json.dumps(result));

    #  给出页面提示请选择注册身份
    result["message"] = "请选择登录身份";
    return HttpResponse(json.dumps(result));


#  定义退出系统方法
def tuichuxitong(request):
    #  清除用户session信息
    request.session.clear();

    #  返回系统登录页面
    return render(request, 'xitong/login.html');


#  定义跳转管理员个人中心
def adminindex(request):
    #  返回管理员个人中心页面
    return render(request, 'xitong/adminindex.html');


#  定义跳转用户个人中心
def userindex(request):
    #  返回用户个人中心页面
    return render(request, 'xitong/userindex.html');


#  定义跳转子女个人中心
def zinvindex(request):
    #  返回子女个人中心页面
    return render(request, 'xitong/zinvindex.html');


#  定义处理管理员修改个人信息的方法
def adminupdategerenxinxiact(request):
    #  获取需要修改的管理员id信息
    id = request.POST.get("id");

    #  根据传入的管理员id信息使用get方法获取管理员信息
    admin = models.Admin.objects.get(id=id);

    #  从POST中获取管理员id信息，并赋值给admin的id字段
    admin.id = request.POST.get("id");

    #  从POST中获取管理员id信息，并赋值给session的id字段
    request.session['id'] = request.POST.get("id");

    #  从POST中获取账号信息，并赋值给admin的username字段
    admin.username = request.POST.get("username");

    #  从POST中获取账号信息，并赋值给session的username字段
    request.session['username'] = request.POST.get("username");

    #  从POST中获取密码信息，并赋值给admin的password字段
    admin.password = request.POST.get("password");

    #  从POST中获取密码信息，并赋值给session的password字段
    request.session['password'] = request.POST.get("password");

    #  使用save方法保存管理员信息
    admin.save();

    #  给出页面提示修改成功，并跳转到管理员个人中心
    return HttpResponse(u"<p>修改成功</p><a href='/loginAndRegist/adminindex'>返回页面</a>");


#  定义处理用户修改个人信息的方法
def userupdategerenxinxiact(request):
    #  获取需要修改的用户id信息
    id = request.POST.get("id");

    #  根据传入的用户id信息使用get方法获取用户信息
    user = models.User.objects.get(id=id);

    #  从POST中获取用户id信息，并赋值给user的id字段
    user.id = request.POST.get("id");

    #  从POST中获取用户id信息，并赋值给session的id字段
    request.session['id'] = request.POST.get("id");

    #  从POST中获取名称信息，并赋值给user的name字段
    user.name = request.POST.get("name");

    #  从POST中获取名称信息，并赋值给session的name字段
    request.session['name'] = request.POST.get("name");

    #  从POST中获取账号信息，并赋值给user的username字段
    user.username = request.POST.get("username");

    #  从POST中获取账号信息，并赋值给session的username字段
    request.session['username'] = request.POST.get("username");

    #  从POST中获取密码信息，并赋值给user的password字段
    user.password = request.POST.get("password");

    #  从POST中获取密码信息，并赋值给session的password字段
    request.session['password'] = request.POST.get("password");

    #  从POST中获取图片信息，并赋值给user的pic字段
    user.pic = request.POST.get("pic");

    #  从POST中获取图片信息，并赋值给session的pic字段
    request.session['pic'] = request.POST.get("pic");

    #  从POST中获取性别信息，并赋值给user的gender字段
    user.gender = request.POST.get("gender");

    #  从POST中获取性别信息，并赋值给session的gender字段
    request.session['gender'] = request.POST.get("gender");

    #  从POST中获取年龄信息，并赋值给user的age字段
    user.age = request.POST.get("age");

    #  从POST中获取年龄信息，并赋值给session的age字段
    request.session['age'] = request.POST.get("age");

    #  从POST中获取身高信息，并赋值给user的shengao字段
    user.shengao = request.POST.get("shengao");

    #  从POST中获取身高信息，并赋值给session的shengao字段
    request.session['shengao'] = request.POST.get("shengao");

    #  从POST中获取体重信息，并赋值给user的tizhong字段
    user.tizhong = request.POST.get("tizhong");

    #  从POST中获取体重信息，并赋值给session的tizhong字段
    request.session['tizhong'] = request.POST.get("tizhong");

    #  从POST中获取电话信息，并赋值给user的tel字段
    user.tel = request.POST.get("tel");

    #  从POST中获取电话信息，并赋值给session的tel字段
    request.session['tel'] = request.POST.get("tel");

    #  从POST中获取锻炼消耗信息，并赋值给user的duanlian字段
    user.duanlian = request.POST.get("duanlian");

    #  从POST中获取锻炼消耗信息，并赋值给session的duanlian字段
    request.session['duanlian'] = request.POST.get("duanlian");

    #  从POST中获取需求卡路里信息，并赋值给user的xuqiu字段
    user.xuqiu = request.POST.get("xuqiu");

    #  从POST中获取需求卡路里信息，并赋值给session的xuqiu字段
    request.session['xuqiu'] = request.POST.get("xuqiu");

    #  使用save方法保存用户信息
    user.save();

    #  给出页面提示修改成功，并跳转到用户个人中心
    return HttpResponse(u"<p>修改成功</p><a href='/loginAndRegist/userindex'>返回页面</a>");


#  定义处理子女修改个人信息的方法
def zinvupdategerenxinxiact(request):
    #  获取需要修改的子女id信息
    id = request.POST.get("id");

    #  根据传入的子女id信息使用get方法获取子女信息
    zinv = models.Zinv.objects.get(id=id);

    #  从POST中获取子女id信息，并赋值给zinv的id字段
    zinv.id = request.POST.get("id");

    #  从POST中获取子女id信息，并赋值给session的id字段
    request.session['id'] = request.POST.get("id");

    #  从POST中获取名字信息，并赋值给zinv的name字段
    zinv.name = request.POST.get("name");

    #  从POST中获取名字信息，并赋值给session的name字段
    request.session['name'] = request.POST.get("name");

    #  从POST中获取账号信息，并赋值给zinv的username字段
    zinv.username = request.POST.get("username");

    #  从POST中获取账号信息，并赋值给session的username字段
    request.session['username'] = request.POST.get("username");

    #  从POST中获取密码信息，并赋值给zinv的password字段
    zinv.password = request.POST.get("password");

    #  从POST中获取密码信息，并赋值给session的password字段
    request.session['password'] = request.POST.get("password");

    #  从POST中获取性别信息，并赋值给zinv的sex字段
    zinv.sex = request.POST.get("sex");

    #  从POST中获取性别信息，并赋值给session的sex字段
    request.session['sex'] = request.POST.get("sex");

    #  从POST中获取电话信息，并赋值给zinv的tel字段
    zinv.tel = request.POST.get("tel");

    #  从POST中获取电话信息，并赋值给session的tel字段
    request.session['tel'] = request.POST.get("tel");

    #  从POST中获取头像信息，并赋值给zinv的pic字段
    zinv.pic = request.POST.get("pic");

    #  从POST中获取头像信息，并赋值给session的pic字段
    request.session['pic'] = request.POST.get("pic");

    #  使用save方法保存子女信息
    zinv.save();

    #  给出页面提示修改成功，并跳转到子女个人中心
    return HttpResponse(u"<p>修改成功</p><a href='/loginAndRegist/zinvindex'>返回页面</a>");
