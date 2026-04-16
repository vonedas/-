# coding:utf-8
from django.db.models import QuerySet, Count
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse
from . import models
import datetime, os, json, random
from openai import OpenAI
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.conf import settings
import base64
from .motiontypeViews import addmotiontype2
from .healthrecordViews import addhealthrecord2

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
            # 检查用户状态
            user = users[0]
            if user.status == "封禁":
                result["message"] = "账号已被封禁，请联系管理员";
                return HttpResponse(json.dumps(result));
                
            #  将登录用户的信息保存到session中
            result["identity"] = identity;

            #  获取当前登录用户的角色信息
            result["userinfo"] = objtodic(user);

            #  获取当前登录用户角色的标识信息
            result["mingzi"] = user.name;

            #  获取当前登录用户角色的id信息
            result["id"] = user.id;

            # 如果用户被禁言，返回特殊消息
            if user.status == "禁言":
                result["message"] = "登录成功，但您的账号已被禁言，部分功能将无法使用";
            else:
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
        status = getQuery(request, "status");
        
        # 获取用户注册时的其他信息
        gender = getQuery(request, "gender");
        age = getQuery(request, "age");
        shengao = getQuery(request, "shengao");
        tizhong = getQuery(request, "tizhong");

        #  如果数据数量大于0
        if (users.count() > 0):

            #  给出用户提示该账号已存在，并跳转到注册页面
            result["message"] = "该账号已存在";
            return HttpResponse(json.dumps(result));
        else:
            # 验证必填字段
            if not all([gender, age, shengao, tizhong]):
                result["message"] = "请填写完整的个人信息";
                return HttpResponse(json.dumps(result));

            #  将传入的用户信息保存到user表中
            user = models.User(
                username=username, 
                password=password,
                status=status,
                gender=gender,
                age=age,
                shengao=shengao,
                tizhong=tizhong
            );
            user.save();

            addmotiontype2("游泳", user.name, user.id);
            addmotiontype2("跑步", user.name, user.id);
            addmotiontype2("跳绳", user.name, user.id);

            addhealthrecord2(user.name,user.id,"血压", user.age,user.gender);
            addhealthrecord2(user.name, user.id, "血糖", user.age, user.gender);
            addhealthrecord2(user.name, user.id, "心率", user.age, user.gender);



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


# AI问答接口
def aidoctor(request):
    result = {}
    try:
        # 获取用户提问内容
        question = getQuery(request, "q")
        if not question:
            result["code"] = "201"
            result["msg"] = "请输入问题内容"
            return HttpResponse(json.dumps(result))

        # 初始化OpenAI客户端
        client = OpenAI(
            api_key='8ae35bc6-9499-4b4e-a953-25d39e8a265c',
            base_url="https://ark.cn-beijing.volces.com/api/v3",
        )

        # 系统提示词
        system_prompt = """你是一个专业的医生助手，请根据用户的问题提供专业、准确的医疗建议。
注意：
1. 回答要简洁明了
2. 对于严重的症状，建议就医
3. 不要做出确定的诊断
4. 提供科学的健康建议
5. 不要使用markdown格式
6. 使用普通文本回复
7. 保持文字格式简单易读"""

        # 创建对话
        completion = client.chat.completions.create(
            model="deepseek-v3-241226",
            temperature=0.82,  # 提高创造性
            top_p=0.88,  # 平衡多样性
            frequency_penalty=0.35,  # 降低重复用词
            presence_penalty=0.6,  # 提高内容新颖性
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        )

        # 获取AI回复
        answer = completion.choices[0].message.content

        result["code"] = "200"
        result["msg"] = answer

    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"服务器错误: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 视频分析接口
def analyzeVideo(request):
    result = {}
    try:
        # 获取视频文件并上传
        video_path = uploadFile(request, "video")

        # 模拟视频分析，随机生成卡路里消耗（100-500之间）
        import random
        calories = random.randint(100, 500)

        result["code"] = "200"
        result["msg"] = "视频分析成功"
        result["videoPath"] = video_path
        result["calories"] = calories

    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"视频处理失败: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 食物图片分析接口
def analyzeFood(request):
    result = {}
    try:
        # 获取图片文件并上传
        photo_path = uploadFile(request, "photo")

        # 模拟食物识别，随机生成卡路里消耗（50-800之间）
        import random
        calories = random.randint(50, 800)

        # 模拟食物名称列表
        food_names = ['苹果', '香蕉', '米饭', '面条', '鸡肉', '鱼', '蔬菜沙拉', '牛排',
                      '三明治', '汉堡', '披萨', '寿司', '炒面', '炒饭', '水果', '蛋糕']
        food_name = random.choice(food_names)

        result["code"] = "200"
        result["msg"] = "识别成功"
        result["photoPath"] = photo_path
        result["calories"] = calories
        result["foodName"] = food_name

    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"识别失败: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 绑定用户接口
def bindElder(request):
    result = {}
    try:
        # 获取子女ID
        childId = getQuery(request, "childId")
        # 获取用户账号
        elderAccount = getQuery(request, "elderAccount")
        # 获取用户密码
        elderPassword = getQuery(request, "elderPassword")

        # 验证用户账号密码
        users = models.User.objects.filter(username=elderAccount, password=elderPassword)
        if users.count() == 0:
            result["code"] = 400
            result["msg"] = "用户账号或密码错误"
            return HttpResponse(json.dumps(result))

        # 获取用户信息
        elder = users[0]

        # 检查是否已经绑定
        existing_bind = models.Bangding.objects.filter(zinvid=childId, userid=elder.id)
        if existing_bind.count() > 0:
            result["code"] = 400
            result["msg"] = "该用户已经绑定"
            return HttpResponse(json.dumps(result))

        # 创建绑定关系
        bind = models.Bangding(
            zinvid=childId,
            userid=elder.id,
            zinv=elderAccount,  # 使用用户账号作为标识
            user=elder.name  # 使用用户姓名作为标识
        )
        bind.save()

        result["code"] = 200
        result["msg"] = "绑定成功"
        result["elder"] = {
            "id": elder.id,
            "name": elder.name,
            "avatar": elder.pic,
            "relation": "子女"
        }

    except Exception as e:
        result["code"] = 500
        result["msg"] = f"绑定失败: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取已绑定用户列表接口
def getElderList(request):
    result = {}
    try:
        # 获取子女ID
        childId = getQuery(request, "childId")

        elders = []
        # 获取所有绑定关系
        bindings = models.Bangding.objects.filter(zinvid=childId, status=1)
        # 获取所有绑定的用户信息
        for bind in bindings:
            user = models.User.objects.get(id=bind.userid)
            elders.append({
                "id": user.id,
                "name": user.name,
                "pic": user.pic,
                "relation": "子女",
                "age": user.age,
            })
        bindings = models.Bangding.objects.filter(userid=childId, status=1)
        for bind in bindings:
            if not any(o["id"]==bind.userid for o in elders):
                user = models.User.objects.get(id=bind.zinvid)
                elders.append({
                    "id": user.id,
                    "name": user.name,
                    "pic": user.pic,
                    "relation": "子女",
                    "age": user.age,
                })

        result["code"] = 200
        result["msg"] = "获取成功"
        result["elders"] = elders

    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取用户信息接口
def getElderInfo(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        user = models.User.objects.get(id=elderId)
        result["code"] = 200
        result["msg"] = "获取成功"
        result["elder"] = objtodic(user)
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取最新血压记录
def getLatestBloodPressure(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        latest = models.Xueya.objects.filter(userid=elderId).order_by('-shijian').first()
        if latest:
            result["code"] = 200
            result["msg"] = "获取成功"
            result["bloodPressure"] = latest.shuzhi
        else:
            result["code"] = 200
            result["msg"] = "暂无记录"
            result["bloodPressure"] = "--"
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取最新体重记录
def getLatestWeight(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        latest = models.Tizhong.objects.filter(userid=elderId).order_by('-shijian').first()
        if latest:
            result["code"] = 200
            result["msg"] = "获取成功"
            result["weight"] = latest.shuju
        else:
            result["code"] = 200
            result["msg"] = "暂无记录"
            result["weight"] = "--"
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取饮食记录
def getDietRecords(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        limit = int(getQuery(request, "limit") or 5)
        records = models.Yinshilog.objects.filter(userid=elderId).order_by('-shijian')[:limit]
        result["code"] = 200
        result["msg"] = "获取成功"
        result["records"] = [objtodic(record) for record in records]
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取运动记录
def getExerciseRecords(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        limit = int(getQuery(request, "limit") or 5)
        records = models.Duanlianlog.objects.filter(userid=elderId).order_by('-shijian')[:limit]
        result["code"] = 200
        result["msg"] = "获取成功"
        result["records"] = [objtodic(record) for record in records]
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取今天是否吃药
def getTodayMedicineStatus(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        today = datetime.datetime.now().date()

        # 查询今天的吃药记录
        medicine_records = models.yao.objects.filter(
            userid=elderId,
            shijian__date=today
        )

        result["code"] = 200
        result["hasTakenMedicine"] = medicine_records.count() > 0
        result["msg"] = "获取成功"
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 获取吃药记录
def getMedicineRecords(request):
    result = {}
    try:
        elderId = getQuery(request, "elderId")
        limit = int(getQuery(request, "limit") or 5)
        records = models.Yao.objects.filter(userid=elderId).order_by('-shijian')[:limit]

        # 获取今天的日期字符串（格式：YYYY-MM-DD）
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        # 检查是否有今天的打卡记录
        has_taken = False
        for record in records:
            if record.daka and today in record.daka:
                has_taken = True
                break

        result["code"] = 200
        result["msg"] = "获取成功"
        result["records"] = [objtodic(record) for record in records]
        result["hasTakenMedicine"] = has_taken
    except Exception as e:
        result["code"] = 500
        result["msg"] = f"获取失败: {str(e)}"
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def analyzeHealthData(request):
    result = {}
    try:
        # 获取请求数据
        data = json.loads(request.body)
        recordType = data.get('recordType')
        timeRange = data.get('timeRange')
        records = data.get('records', [])
        shangxian = data.get('shangxian')  # 获取上限值
        xiaxian = data.get('xiaxian')  # 获取下限值

        if not records:
            result["code"] = "201"
            result["msg"] = "没有可分析的数据"
            return HttpResponse(json.dumps(result))

        # 构建分析提示词
        prompt = f"""请分析以下健康数据：
记录类型：{recordType}
时间范围：{timeRange}
正常值范围：{xiaxian} - {shangxian}
数据记录：{json.dumps(records, ensure_ascii=False)}

请提供以下分析：
1. 数据趋势分析
2. 异常值识别（基于正常值范围 {xiaxian} - {shangxian}）
3. 健康建议
4. 注意事项

请用简洁明了的语言回答，避免使用专业术语。"""

        # 初始化Ark客户端
        client = OpenAI(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            api_key="8ae35bc6-9499-4b4e-a953-25d39e8a265c"
        )

        # 创建对话
        completion = client.chat.completions.create(
            model="deepseek-v3-250324",
            messages=[
                {"role": "system", "content": "你是一个专业的健康数据分析师，请根据提供的数据进行专业分析。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            top_p=0.8
        )

        # 获取分析结果
        analysis = completion.choices[0].message.content

        result["code"] = "200"
        result["msg"] = "分析成功"
        result["analysis"] = analysis

    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"分析失败: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))


@csrf_exempt
def upload_image(request):
    """
    富文本编辑器的图片上传接口
    """
    result = {
        "errno": 1,  # 1 表示失败，0 表示成功
        "data": []
    }

    try:
        # 获取上传的文件
        file_obj = request.FILES.get('image')

        if file_obj is None:
            result["message"] = "请选择要上传的图片"
            return HttpResponse(json.dumps(result))

        # 获取文件扩展名
        ext = file_obj.name.split('.')[-1].lower()

        # 验证文件类型
        allowed_types = ['jpg', 'jpeg', 'png', 'gif', 'webp']
        if ext not in allowed_types:
            result["message"] = "只允许上传 jpg、jpeg、png、gif、webp 格式的图片"
            return HttpResponse(json.dumps(result))

        # 验证文件大小（限制为 5MB）
        if file_obj.size > 5 * 1024 * 1024:
            result["message"] = "图片大小不能超过 5MB"
            return HttpResponse(json.dumps(result))

        # 生成随机文件名
        filename = f'article_img_{int(time.time())}_{random.randint(1000, 9999)}.{ext}'

        # 构建文件保存路径（相对于 MEDIA_ROOT 目录）
        relative_path = os.path.join('article_images', filename)
        absolute_path = os.path.join(settings.MEDIA_ROOT, 'article_images', filename)

        # 确保目录存在
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

        # 写入文件
        with open(absolute_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        # 构建图片访问URL
        image_url = f'/media/article_images/{filename}'

        # 返回成功响应
        result["errno"] = 0
        result["data"] = {
            "url": image_url,
            "alt": filename,
            "href": image_url
        }

    except Exception as e:
        result["message"] = f"上传失败：{str(e)}"

    return HttpResponse(json.dumps(result))

# 禁言用户
def muteUser(request, id):
    try:
        # 获取用户信息
        user = models.User.objects.get(id=id)
        # 设置状态为禁言
        user.status = "禁言"
        user.save()
        # 返回成功信息
        return HttpResponse("<script>alert('禁言成功');window.location.href='/user/usermanage';</script>")
    except Exception as e:
        # 返回错误信息
        return HttpResponse("<script>alert('操作失败：" + str(e) + "');window.location.href='/user/usermanage';</script>")

# 封禁用户
def banUser(request, id):
    try:
        # 获取用户信息
        user = models.User.objects.get(id=id)
        # 设置状态为封禁
        user.status = "封禁"
        user.save()
        # 返回成功信息
        return HttpResponse("<script>alert('封禁成功');window.location.href='/user/usermanage';</script>")
    except Exception as e:
        # 返回错误信息
        return HttpResponse("<script>alert('操作失败：" + str(e) + "');window.location.href='/user/usermanage';</script>")

# 恢复用户状态
def restoreUser(request, id):
    try:
        # 获取用户信息
        user = models.User.objects.get(id=id)
        # 设置状态为正常
        user.status = "正常"
        user.save()
        # 返回成功信息
        return HttpResponse("<script>alert('恢复成功');window.location.href='/user/usermanage';</script>")
    except Exception as e:
        # 返回错误信息
        return HttpResponse("<script>alert('操作失败：" + str(e) + "');window.location.href='/user/usermanage';</script>")

# 获取文章分类统计
def getArticleCategories(request):
    try:
        # 获取所有文章分类
        article_types = models.Articletype.objects.all()
        
        data = []
        for article_type in article_types:
            # 统计每个分类下的文章数量
            count = models.Article.objects.filter(
                articletypeid=article_type.id
            ).count()
            
            # 只添加有文章的分类
            if count > 0:
                data.append({
                    'name': article_type.name,
                    'value': count
                })
        
        # 如果没有任何分类有文章，返回空列表
        if not data:
            return HttpResponse(json.dumps([]))
            
        return HttpResponse(json.dumps(data, ensure_ascii=False))
    except Exception as e:
        print(f"Error in getArticleCategories: {str(e)}")
        return HttpResponse(json.dumps([]))

# 获取用户状态统计
def getUserStatus(request):
    try:
        # 统计各状态的用户数量
        status_counts = models.User.objects.values('status').annotate(count=Count('id'))
        
        # 格式化数据
        data = [
            {'name': status['status'] or '正常', 'value': status['count']} 
            for status in status_counts
        ]
        
        return HttpResponse(json.dumps(data, ensure_ascii=False))
    except Exception as e:
        return HttpResponse(json.dumps([]))

# 获取健康记录趋势
def getHealthTrend(request):
    try:
        # 获取最近7天的日期列表
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=6)
        dates = []
        normal_counts = []
        abnormal_counts = []
        
        # 对每一天进行统计
        current_date = start_date
        while current_date <= end_date:
            date_str = current_date.strftime('%Y-%m-%d')
            dates.append(date_str)
            
            # 获取当天的记录
            day_records = models.Recordhealth.objects.filter(
                recordtime__startswith=date_str
            )
            
            # 统计正常和异常记录
            normal_count = 0
            abnormal_count = 0
            for record in day_records:
                try:
                    value = float(record.value)
                    shangxian = float(record.shangxian) if record.shangxian else float('inf')
                    xiaxian = float(record.xiaxian) if record.xiaxian else float('-inf')
                    
                    if xiaxian <= value <= shangxian:
                        normal_count += 1
                    else:
                        abnormal_count += 1
                except (ValueError, TypeError):
                    continue
            
            normal_counts.append(normal_count)
            abnormal_counts.append(abnormal_count)
            
            current_date += datetime.timedelta(days=1)
        
        data = {
            'dates': dates,
            'normal': normal_counts,
            'abnormal': abnormal_counts
        }
        
        return HttpResponse(json.dumps(data, ensure_ascii=False))
    except Exception as e:
        return HttpResponse(json.dumps({'dates': [], 'normal': [], 'abnormal': []}))

def keshihua(request):
    #  返回登录页面
    return render(request, 'xitong/keshihua.html');

# 图片分析接口
def analyzeImage(request):
    result = {}
    try:
        # 获取上传的图片文件
        image_file = request.FILES.get('image')
        if not image_file:
            result["code"] = "201"
            result["msg"] = "请上传图片"
            return HttpResponse(json.dumps(result))

        # 保存图片到临时目录
        temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp_images')
        os.makedirs(temp_dir, exist_ok=True)
        
        # 生成唯一的文件名
        file_name = f'temp_{int(time.time())}_{random.randint(1000, 9999)}.jpg'
        file_path = os.path.join(temp_dir, file_name)
        
        with open(file_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        # 初始化智谱AI客户端
        client = OpenAI(
            api_key="482c49d2cd7c46959c147cf8a6a992ee.C4oxo0locwuHyhq3",
            base_url="https://open.bigmodel.cn/api/paas/v4/"
        )

        # 读取图片文件为base64
        with open(file_path, 'rb') as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

        # 构建提示词
        prompt = """请分析这张图片，提供以下信息：
1. 图片的主要内容描述
2. 与健康相关的建议
3. 需要注意的事项

请用简洁明了的语言回答。"""

        # 调用智谱AI进行图片分析
        completion = client.chat.completions.create(
            model="glm-4v",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )

        # 获取AI回复
        answer = completion.choices[0].message.content

        # 删除临时文件
        try:
            os.remove(file_path)
        except:
            pass

        result["code"] = "200"
        result["msg"] = answer

    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"分析失败: {str(e)}"

    return HttpResponse(json.dumps(result, ensure_ascii=False))

def getRankingData(request):
    result = {}
    try:
        # 获取当前用户ID
        userid = getQuery(request, "userid")
        if not userid:
            result["code"] = "201"
            result["msg"] = "用户ID不能为空"
            return HttpResponse(json.dumps(result))

        # 获取当前日期
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # 获取当前用户信息
        current_user = models.User.objects.get(id=userid)
        
        # 获取所有好友ID（包括自己）
        friend_ids = [userid]  # 先加入自己
        bindings = models.Bangding.objects.filter(zinvid=userid, status=1)
        for binding in bindings:
            auth = models.Auth.objects.filter(userid=binding.userid, authid=binding.zinvid, xuqiu=False)
            if auth.count() == 0:
                friend_ids.append(binding.userid)
        bindings = models.Bangding.objects.filter(userid=userid, status=1)
        for binding in bindings:
            if not any(fid==binding.userid for fid in friend_ids):
                auth = models.Auth.objects.filter(userid=binding.userid, authid=binding.zinvid, xuqiu=False)
                if auth.count() == 0:
                    friend_ids.append(binding.zinvid)
        
        # 获取所有好友信息
        friends = models.User.objects.filter(id__in=friend_ids)
        
        ranking_data = []
        for friend in friends:
            # 获取今日运动记录
            exercise_records = models.Duanlianlog.objects.filter(
                userid=friend.id,
                shijian__startswith=today
            )
            total_exercise_calories = sum(float(record.kaluli) for record in exercise_records)
            
            # 获取今日饮食记录
            diet_records = models.Yinshilog.objects.filter(
                userid=friend.id,
                shijian__startswith=today
            )
            total_diet_calories = sum(float(record.kaluli) for record in diet_records)
            
            # 计算运动得分
            target_exercise = float(friend.duanlian) if friend.duanlian else 0
            if target_exercise > 0:
                if total_exercise_calories >= target_exercise:
                    exercise_score = 100.00
                    exercise_status = "您已达到目标，请注意休息"
                else:
                    exercise_score = round((total_exercise_calories / target_exercise) * 100, 2)
                    exercise_status = "继续加油"
            else:
                exercise_score = 0
                exercise_status = "未设置目标"
            
            # 计算饮食得分
            target_diet = float(friend.xuqiu) if friend.xuqiu else 0
            if target_diet > 0:
                if total_diet_calories <= target_diet:
                    # 未超标情况：正常计算百分比
                    diet_score = round((total_diet_calories / target_diet) * 100, 2)
                    diet_status = "继续加油"
                else:
                    # 超标情况：计算负分
                    excess = total_diet_calories - target_diet
                    diet_score = round((target_diet / total_diet_calories) * 100, 2)
                    if total_diet_calories > target_diet + 1000:
                        diet_status = "过量饮食，请注意"
                    else:
                        diet_status = "已超出目标"
            else:
                diet_score = 0
                diet_status = "未设置目标"
            
            ranking_data.append({
                "id": friend.id,
                "name": friend.name,
                "pic": friend.pic,
                "exercise": {
                    "score": exercise_score,
                    "status": exercise_status,
                    "total": total_exercise_calories,
                    "target": target_exercise
                },
                "diet": {
                    "score": diet_score,
                    "status": diet_status,
                    "total": total_diet_calories,
                    "target": target_diet
                }
            })
        
        # 按运动得分排序
        exercise_ranking = sorted(ranking_data, key=lambda x: x["exercise"]["score"], reverse=True)
        # 按饮食得分排序
        diet_ranking = sorted(ranking_data, key=lambda x: x["diet"]["score"], reverse=True)
        
        result["code"] = "200"
        result["msg"] = "获取成功"
        result["data"] = {
            "exerciseRanking": exercise_ranking,
            "dietRanking": diet_ranking
        }
        
    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"获取失败: {str(e)}"
    
    return HttpResponse(json.dumps(result, ensure_ascii=False))

# 获取验证码
def getVerificationCode(request):
    result = {}
    try:
        # 生成4位随机数字
        code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        
        result["code"] = "200"
        result["msg"] = "获取成功"
        result["verificationCode"] = code
        
    except Exception as e:
        result["code"] = "500"
        result["msg"] = f"获取失败: {str(e)}"
    
    return HttpResponse(json.dumps(result, ensure_ascii=False))
