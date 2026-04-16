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


#    定义添加运动类型的方法，响应页面请求
def addmotiontype(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加运动类型页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addmotiontype.html', {'userall': userall, });


#  处理添加运动类型方法   
def addmotiontypeact(request):
    #  从页面post数据中获取运动类型
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取单位
    danweistr = request.POST.get("danwei");
    danwei = "";
    if (danweistr is not None):
        danwei = danweistr;

    #  从页面post数据中获取运动值
    valuestr = request.POST.get("value");
    value = "";
    if (valuestr is not None):
        value = valuestr;

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

    #  将运动类型的属性赋值给运动类型，生成运动类型对象
    motiontype = models.Motiontype(name=name, danwei=danwei, value=value, user=user, userid=userid, );

    #  调用save方法保存运动类型信息
    motiontype.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加运动类型成功,并跳转到运动类型管理页面
    return HttpResponse(u"<p>添加运动类型成功</p><a href='/motiontype/motiontypemanage'>返回页面</a>");


#  定义表名管理方法，响应页面motiontypemanage请求   
def motiontypemanage(request):
    #  通过all方法查询所有的运动类型信息
    motiontypeall = models.Motiontype.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到运动类型管理页面，并附带所有运动类型信息
    return render(request, 'xitong/motiontypemanage.html', {'motiontypeall': motiontypeall});


#  定义表名查看方法，响应页面motiontypeview请求   
def motiontypeview(request):
    #  通过all方法查询所有的运动类型信息
    motiontypeall = models.Motiontype.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到运动类型查看页面，并附带所有运动类型信息
    return render(request, 'xitong/motiontypeview.html', {'motiontypeall': motiontypeall});


#  定义修改运动类型方法，通过id查询对应的运动类型信息，返回页面展示  
def updatemotiontype(request, id):
    #  使用get方法，通过id查询对应的运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改运动类型页面，并附带当前运动类型信息
    return render(request, 'xitong/updatemotiontype.html', {'motiontype': motiontype, 'userall': userall, });


#  定义处理修改运动类型方法   
def updatemotiontypeact(request):
    #  使用request获取post中的运动类型id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的运动类型id获取对应的运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);

    #  从页面post数据中获取运动类型并赋值给motiontype的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        motiontype.name = namestr;

    #  从页面post数据中获取单位并赋值给motiontype的danwei字段
    danweistr = request.POST.get("danwei");
    if (danweistr is not None):
        motiontype.danwei = danweistr;

    #  从页面post数据中获取运动值并赋值给motiontype的value字段
    valuestr = request.POST.get("value");
    if (valuestr is not None):
        motiontype.value = valuestr;

    #  从页面post数据中获取用户并赋值给motiontype的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        motiontype.user = userstr;

    #  从页面post数据中获取用户id并赋值给motiontype的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        motiontype.userid = useridstr;

    #  调用save方法保存运动类型信息
    motiontype.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改运动类型成功,并跳转到运动类型管理页面
    return HttpResponse(u"<p>修改运动类型成功</p><a href='/motiontype/motiontypemanage'>返回页面</a>");


#  定义删除运动类型方法   
def deletemotiontypeact(request, id):
    #  调用django的delete方法，根据id删除运动类型信息
    models.Motiontype.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除运动类型成功,并跳转到运动类型管理页面
    return HttpResponse(u"<p>删除运动类型成功</p><a href='/motiontype/motiontypemanage'>返回页面</a>");


#  定义搜索运动类型方法，响应页面搜索请求   
def searchmotiontype(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的运动类型信息
    motiontypeall = models.Motiontype.objects.filter(name__icontains=search);

    #  跳转到搜索运动类型页面，并附带查询的运动类型信息
    return render(request, 'xitong/searchmotiontype.html', {"motiontypeall": motiontypeall});


#  处理运动类型详情   
def motiontypedetails(request, id):
    #  根据页面传入id获取运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到运动类型详情页面,并运动类型信息传递到页面中
    return render(request, 'xitong/motiontypedetails.html', {"motiontype": motiontype});


#  定义跳转user添加运动类型页面的方法  
def useraddmotiontype(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加运动类型页面
    return render(request, 'xitong/useraddmotiontype.html', {'userall': userall, });


#  处理添加运动类型方法   
def useraddmotiontypeact(request):
    #  从页面post数据中获取运动类型
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取单位
    danweistr = request.POST.get("danwei");
    danwei = "";
    if (danweistr is not None):
        danwei = danweistr;

    #  从页面post数据中获取运动值
    valuestr = request.POST.get("value");
    value = "";
    if (valuestr is not None):
        value = valuestr;

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

    #  将运动类型的属性赋值给运动类型，生成运动类型对象
    motiontype = models.Motiontype(name=name, danwei=danwei, value=value, user=user, userid=userid, );

    #  调用save方法保存运动类型信息
    motiontype.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加运动类型成功,并跳转到运动类型管理页面
    return HttpResponse(u"<p>添加运动类型成功</p><a href='/motiontype/usermotiontypemanage'>返回页面</a>");


#  跳转user运动类型管理页面
def usermotiontypemanage(request):
    #  查询出userid等于当前用户id的所有运动类型信息
    motiontypeall = models.Motiontype.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回运动类型管理页面，并携带motiontypeall的数据信息
    return render(request, 'xitong/usermotiontypemanage.html', {'motiontypeall': motiontypeall});


#  定义跳转user修改运动类型页面      
def userupdatemotiontype(request, id):
    #  根据页面传入的运动类型id信息，查询出对应的运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改运动类型页面，并携带查询出的运动类型信息
    return render(request, 'xitong/userupdatemotiontype.html', {'motiontype': motiontype, 'userall': userall, });


#  定义处理修改运动类型方法   
def userupdatemotiontypeact(request):
    #  使用request获取post中的运动类型id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的运动类型id获取对应的运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);

    #  从页面post数据中获取运动类型并赋值给motiontype的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        motiontype.name = namestr;

    #  从页面post数据中获取单位并赋值给motiontype的danwei字段
    danweistr = request.POST.get("danwei");
    if (danweistr is not None):
        motiontype.danwei = danweistr;

    #  从页面post数据中获取运动值并赋值给motiontype的value字段
    valuestr = request.POST.get("value");
    if (valuestr is not None):
        motiontype.value = valuestr;

    #  从页面post数据中获取用户并赋值给motiontype的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        motiontype.user = userstr;

    #  从页面post数据中获取用户id并赋值给motiontype的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        motiontype.userid = useridstr;

    #  调用save方法保存运动类型信息
    motiontype.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改运动类型成功,并跳转到运动类型管理页面
    return HttpResponse(u"<p>修改运动类型成功</p><a href='/motiontype/usermotiontypemanage'>返回页面</a>");


#  定义user删除运动类型信息
def userdeletemotiontypeact(request, id):
    #  根据页面传入的运动类型id信息，删除出对应的运动类型信息
    models.Motiontype.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除运动类型成功，并跳转到运动类型管理页面
    return HttpResponse(u"<p>删除运动类型成功</p><a href='/motiontype/usermotiontypemanage'>返回页面</a>");


#  处理添加运动类型Json方法
def addmotiontypeactjson(request):
    result = {}
    # 从request中获取运动类型信息
    name = getQuery(request, "name")
    # 从request中获取用户信息
    user = getQuery(request, "user")
    # 从request中获取用户id信息
    userid = getQuery(request, "userid")

    # 调用deepseek Ark生成运动类型每分钟消耗的卡路里值

    client = OpenAI(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key="8ae35bc6-9499-4b4e-a953-25d39e8a265c",
    )
    prompt = f"请根据运动名称'{name}'，提供该运动每分钟消耗的卡路里值（千卡）。请只返回一个数字，不要包含单位。"
    try:
        completion = client.chat.completions.create(
            model="deepseek-v3-250324",
            messages=[
                {"role": "system", "content": "你是一个专业的运动健康顾问，请根据运动名称提供准确的每分钟卡路里消耗值。"},
                {"role": "user", "content": prompt},
            ],
        )
        ai_result = completion.choices[0].message.content.strip()
        try:
            value = float(ai_result)
        except:
            value = 5
    except Exception as e:
        print(f"AI调用失败: {str(e)}")
        value = 5

    # 固定单位为"千卡/分钟"
    danwei = "千卡/分钟"

    #  将运动类型的属性赋值给运动类型，生成运动类型对象
    motiontype = models.Motiontype(name=name, danwei=danwei, value=value, user=user, userid=userid, )

    #  调用save方法保存运动类型信息
    motiontype.save()
    result['message'] = "添加运动类型成功"
    result['code'] = "202"

    #  返回添加运动类型的结果
    return HttpResponse(json.dumps(result))


from openai import OpenAI


#  处理添加运动类型Json方法
def addmotiontype2(name, user ,userid):
    result = {}

    # 调用deepseek Ark生成运动类型每分钟消耗的卡路里值

    client = OpenAI(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key="8ae35bc6-9499-4b4e-a953-25d39e8a265c",
    )
    prompt = f"请根据运动名称'{name}'，提供该运动每分钟消耗的卡路里值（千卡）。请只返回一个数字，不要包含单位。"
    try:
        completion = client.chat.completions.create(
            model="deepseek-v3-250324",
            messages=[
                {"role": "system", "content": "你是一个专业的运动健康顾问，请根据运动名称提供准确的每分钟卡路里消耗值。"},
                {"role": "user", "content": prompt},
            ],
        )
        ai_result = completion.choices[0].message.content.strip()
        try:
            value = float(ai_result)
        except:
            value = 5
    except Exception as e:
        print(f"AI调用失败: {str(e)}")
        value = 5

    # 固定单位为"千卡/分钟"
    danwei = "千卡/分钟"

    #  将运动类型的属性赋值给运动类型，生成运动类型对象
    motiontype = models.Motiontype(name=name, danwei=danwei, value=value, user=user, userid=userid, )

    #  调用save方法保存运动类型信息
    motiontype.save()




#  定义处理修改运动类型方法   
def updatemotiontypeactjson(request):
    result = {};

    #  使用request获取post中的运动类型id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的运动类型id获取对应的运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);
    # 从request中获取运动类型信息
    name = getQuery(request, "name");
    # 如果request中存在运动类型信息，赋值给运动类型
    if (name != ""):
        motiontype.name = name;
    # 从request中获取单位信息
    danwei = getQuery(request, "danwei");
    # 如果request中存在单位信息，赋值给运动类型
    if (danwei != ""):
        motiontype.danwei = danwei;
    # 从request中获取运动值信息
    value = getQuery(request, "value");
    # 如果request中存在运动值信息，赋值给运动类型
    if (value != ""):
        motiontype.value = value;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给运动类型
    if (user != ""):
        motiontype.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给运动类型
    if (userid != ""):
        motiontype.userid = userid;

    #  调用save方法保存运动类型信息
    motiontype.save();
    result['message'] = "修改运动类型成功"
    result['code'] = "202"

    #  返回修改运动类型的结果
    return HttpResponse(json.dumps(result));


#  定义删除运动类型方法   
def deletemotiontypejson(request):
    result = {};

    #  使用request获取post中的运动类型id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除运动类型信息
    models.Motiontype.objects.filter(id=id).delete();
    result['message'] = "删除运动类型成功"
    result['code'] = "202"

    #  返回删除运动类型的结果
    return HttpResponse(json.dumps(result));


#  定义搜索运动类型json方法，响应页面搜索请求   
def searchmotiontypejson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的运动类型信息
    motiontypeall = models.Motiontype.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的运动类型信息
    result['motiontypeall'] = objtodic(motiontypeall)
    result['message'] = "查询运动类型成功"
    result['code'] = "202"

    #  返回查询运动类型的结果
    return HttpResponse(json.dumps(result));



#  定义搜索运动类型json方法，响应页面搜索请求
def usersearchmotiontypejson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    userid = getQuery(request, "userid");

    #  使用django的filter方法过滤查询包含search的运动类型信息
    motiontypeall = models.Motiontype.objects.filter(name__icontains=search, userid=userid);

    #  返回查询结果，附带查询的运动类型信息
    result['motiontypeall'] = objtodic(motiontypeall)
    result['message'] = "查询运动类型成功"
    result['code'] = "202"

    #  返回查询运动类型的结果
    return HttpResponse(json.dumps(result));

#  处理运动类型详情   
def motiontypedetailsjson(request):
    result = {};

    #  使用request获取post中的运动类型id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取运动类型信息
    motiontype = models.Motiontype.objects.get(id=id);
    result['motiontype'] = objtodic(motiontype);
    result['message'] = "查询运动类型成功"
    result['code'] = "202"

    #  返回查询运动类型详情的结果
    return HttpResponse(json.dumps(result));
