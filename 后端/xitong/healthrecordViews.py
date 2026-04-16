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


#    定义添加健康记录类型的方法，响应页面请求
def addhealthrecord(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加健康记录类型页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addhealthrecord.html', {'userall': userall, });


#  处理添加健康记录类型方法   
def addhealthrecordact(request):
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

    #  从页面post数据中获取记录类型
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取上限值
    shangxianstr = request.POST.get("shangxian");
    shangxian = "";
    if (shangxianstr is not None):
        shangxian = shangxianstr;

    #  从页面post数据中获取下限值
    xiaxianstr = request.POST.get("xiaxian");
    xiaxian = "";
    if (xiaxianstr is not None):
        xiaxian = xiaxianstr;

    #  从页面post数据中获取单位
    danweistr = request.POST.get("danwei");
    danwei = "";
    if (danweistr is not None):
        danwei = danweistr;

    #  将健康记录类型的属性赋值给健康记录类型，生成健康记录类型对象
    healthrecord = models.Healthrecord(user=user, userid=userid, name=name, shangxian=shangxian, xiaxian=xiaxian,
                                       danwei=danwei, );

    #  调用save方法保存健康记录类型信息
    healthrecord.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加健康记录类型成功,并跳转到健康记录类型管理页面
    return HttpResponse(u"<p>添加健康记录类型成功</p><a href='/healthrecord/healthrecordmanage'>返回页面</a>");


#  定义表名管理方法，响应页面healthrecordmanage请求   
def healthrecordmanage(request):
    #  通过all方法查询所有的健康记录类型信息
    healthrecordall = models.Healthrecord.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到健康记录类型管理页面，并附带所有健康记录类型信息
    return render(request, 'xitong/healthrecordmanage.html', {'healthrecordall': healthrecordall});


#  定义表名查看方法，响应页面healthrecordview请求   
def healthrecordview(request):
    #  通过all方法查询所有的健康记录类型信息
    healthrecordall = models.Healthrecord.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到健康记录类型查看页面，并附带所有健康记录类型信息
    return render(request, 'xitong/healthrecordview.html', {'healthrecordall': healthrecordall});


#  定义修改健康记录类型方法，通过id查询对应的健康记录类型信息，返回页面展示  
def updatehealthrecord(request, id):
    #  使用get方法，通过id查询对应的健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改健康记录类型页面，并附带当前健康记录类型信息
    return render(request, 'xitong/updatehealthrecord.html', {'healthrecord': healthrecord, 'userall': userall, });


#  定义处理修改健康记录类型方法   
def updatehealthrecordact(request):
    #  使用request获取post中的健康记录类型id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的健康记录类型id获取对应的健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给healthrecord的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        healthrecord.user = userstr;

    #  从页面post数据中获取用户id并赋值给healthrecord的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        healthrecord.userid = useridstr;

    #  从页面post数据中获取记录类型并赋值给healthrecord的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        healthrecord.name = namestr;

    #  从页面post数据中获取上限值并赋值给healthrecord的shangxian字段
    shangxianstr = request.POST.get("shangxian");
    if (shangxianstr is not None):
        healthrecord.shangxian = shangxianstr;

    #  从页面post数据中获取下限值并赋值给healthrecord的xiaxian字段
    xiaxianstr = request.POST.get("xiaxian");
    if (xiaxianstr is not None):
        healthrecord.xiaxian = xiaxianstr;

    #  从页面post数据中获取单位并赋值给healthrecord的danwei字段
    danweistr = request.POST.get("danwei");
    if (danweistr is not None):
        healthrecord.danwei = danweistr;

    #  调用save方法保存健康记录类型信息
    healthrecord.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改健康记录类型成功,并跳转到健康记录类型管理页面
    return HttpResponse(u"<p>修改健康记录类型成功</p><a href='/healthrecord/healthrecordmanage'>返回页面</a>");


#  定义删除健康记录类型方法   
def deletehealthrecordact(request, id):
    #  调用django的delete方法，根据id删除健康记录类型信息
    models.Healthrecord.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除健康记录类型成功,并跳转到健康记录类型管理页面
    return HttpResponse(u"<p>删除健康记录类型成功</p><a href='/healthrecord/healthrecordmanage'>返回页面</a>");


#  定义搜索健康记录类型方法，响应页面搜索请求   
def searchhealthrecord(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的健康记录类型信息
    healthrecordall = models.Healthrecord.objects.filter(user__icontains=search);

    #  跳转到搜索健康记录类型页面，并附带查询的健康记录类型信息
    return render(request, 'xitong/searchhealthrecord.html', {"healthrecordall": healthrecordall});


#  处理健康记录类型详情   
def healthrecorddetails(request, id):
    #  根据页面传入id获取健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到健康记录类型详情页面,并健康记录类型信息传递到页面中
    return render(request, 'xitong/healthrecorddetails.html', {"healthrecord": healthrecord});


#  定义跳转user添加健康记录类型页面的方法  
def useraddhealthrecord(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加健康记录类型页面
    return render(request, 'xitong/useraddhealthrecord.html', {'userall': userall, });


#  处理添加健康记录类型方法   
def useraddhealthrecordact(request):
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

    #  从页面post数据中获取记录类型
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取上限值
    shangxianstr = request.POST.get("shangxian");
    shangxian = "";
    if (shangxianstr is not None):
        shangxian = shangxianstr;

    #  从页面post数据中获取下限值
    xiaxianstr = request.POST.get("xiaxian");
    xiaxian = "";
    if (xiaxianstr is not None):
        xiaxian = xiaxianstr;

    #  从页面post数据中获取单位
    danweistr = request.POST.get("danwei");
    danwei = "";
    if (danweistr is not None):
        danwei = danweistr;

    #  将健康记录类型的属性赋值给健康记录类型，生成健康记录类型对象
    healthrecord = models.Healthrecord(user=user, userid=userid, name=name, shangxian=shangxian, xiaxian=xiaxian,
                                       danwei=danwei, );

    #  调用save方法保存健康记录类型信息
    healthrecord.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加健康记录类型成功,并跳转到健康记录类型管理页面
    return HttpResponse(u"<p>添加健康记录类型成功</p><a href='/healthrecord/userhealthrecordmanage'>返回页面</a>");


#  跳转user健康记录类型管理页面
def userhealthrecordmanage(request):
    #  查询出userid等于当前用户id的所有健康记录类型信息
    healthrecordall = models.Healthrecord.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回健康记录类型管理页面，并携带healthrecordall的数据信息
    return render(request, 'xitong/userhealthrecordmanage.html', {'healthrecordall': healthrecordall});


#  定义跳转user修改健康记录类型页面      
def userupdatehealthrecord(request, id):
    #  根据页面传入的健康记录类型id信息，查询出对应的健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改健康记录类型页面，并携带查询出的健康记录类型信息
    return render(request, 'xitong/userupdatehealthrecord.html', {'healthrecord': healthrecord, 'userall': userall, });


#  定义处理修改健康记录类型方法   
def userupdatehealthrecordact(request):
    #  使用request获取post中的健康记录类型id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的健康记录类型id获取对应的健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给healthrecord的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        healthrecord.user = userstr;

    #  从页面post数据中获取用户id并赋值给healthrecord的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        healthrecord.userid = useridstr;

    #  从页面post数据中获取记录类型并赋值给healthrecord的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        healthrecord.name = namestr;

    #  从页面post数据中获取上限值并赋值给healthrecord的shangxian字段
    shangxianstr = request.POST.get("shangxian");
    if (shangxianstr is not None):
        healthrecord.shangxian = shangxianstr;

    #  从页面post数据中获取下限值并赋值给healthrecord的xiaxian字段
    xiaxianstr = request.POST.get("xiaxian");
    if (xiaxianstr is not None):
        healthrecord.xiaxian = xiaxianstr;

    #  从页面post数据中获取单位并赋值给healthrecord的danwei字段
    danweistr = request.POST.get("danwei");
    if (danweistr is not None):
        healthrecord.danwei = danweistr;

    #  调用save方法保存健康记录类型信息
    healthrecord.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改健康记录类型成功,并跳转到健康记录类型管理页面
    return HttpResponse(u"<p>修改健康记录类型成功</p><a href='/healthrecord/userhealthrecordmanage'>返回页面</a>");


#  定义user删除健康记录类型信息
def userdeletehealthrecordact(request, id):
    #  根据页面传入的健康记录类型id信息，删除出对应的健康记录类型信息
    models.Healthrecord.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除健康记录类型成功，并跳转到健康记录类型管理页面
    return HttpResponse(u"<p>删除健康记录类型成功</p><a href='/healthrecord/userhealthrecordmanage'>返回页面</a>");


#  处理添加健康记录类型Json方法
def addhealthrecordactjson(request):
    import os
    from openai import OpenAI

    result = {}
    user = getQuery(request, "user")
    userid = getQuery(request, "userid")
    name = getQuery(request, "name")
    age = getQuery(request, "age")
    gender = getQuery(request, "gender")

    # 1. 组装AI提问内容
    prompt = f"请根据医学常识，给出{age}岁{gender}性人群的{name}的正常值范围和常用单位，只需返回下限-上限+空格+单位，例如：90-140 mmHg，不要返回其他内容。"

    # 2. 调用deepseek
    client = OpenAI(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key="8ae35bc6-9499-4b4e-a953-25d39e8a265c",
    )
    completion = client.chat.completions.create(
        model="deepseek-v3-250324",
        messages=[
            {"role": "system", "content": "你是人工智能健康助手。"},
            {"role": "user", "content": prompt},
        ],
    )
    ai_result = completion.choices[0].message.content.strip()

    # 3. 解析AI返回的范围和单位
    import re
    shangxian, xiaxian, danwei = "", "", ""
    match = re.match(r"([0-9.]+)[-~—]+([0-9.]+)\s*([^\s]+.*)", ai_result)
    if match:
        xiaxian, shangxian, danwei = match.groups()
    else:
        xiaxian, shangxian, danwei = "", "", ""

    # 4. 保存到数据库
    healthrecord = models.Healthrecord(
        user=user,
        userid=userid,
        name=name,
        shangxian=shangxian,
        xiaxian=xiaxian,
        danwei=danwei,
    )
    healthrecord.save()
    result['message'] = "添加健康记录类型成功"
    result['code'] = "202"
    return HttpResponse(json.dumps(result))







#  处理添加健康记录类型Json方法
def addhealthrecord2(user,userid,name,age,gender):
    import os
    from openai import OpenAI

    result = {}


    # 1. 组装AI提问内容
    prompt = f"请根据医学常识，给出{age}岁{gender}性人群的{name}的正常值范围和常用单位，只需返回下限-上限+空格+单位，例如：90-140 mmHg，不要返回其他内容。"

    # 2. 调用deepseek
    client = OpenAI(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key="8ae35bc6-9499-4b4e-a953-25d39e8a265c",
    )
    completion = client.chat.completions.create(
        model="deepseek-v3-250324",
        messages=[
            {"role": "system", "content": "你是人工智能健康助手。"},
            {"role": "user", "content": prompt},
        ],
    )
    ai_result = completion.choices[0].message.content.strip()

    # 3. 解析AI返回的范围和单位
    import re
    shangxian, xiaxian, danwei = "", "", ""
    match = re.match(r"([0-9.]+)[-~—]+([0-9.]+)\s*([^\s]+.*)", ai_result)
    if match:
        xiaxian, shangxian, danwei = match.groups()
    else:
        xiaxian, shangxian, danwei = "", "", ""

    # 4. 保存到数据库
    healthrecord = models.Healthrecord(
        user=user,
        userid=userid,
        name=name,
        shangxian=shangxian,
        xiaxian=xiaxian,
        danwei=danwei,
    )
    healthrecord.save()


#  定义处理修改健康记录类型方法   
def updatehealthrecordactjson(request):
    result = {};

    #  使用request获取post中的健康记录类型id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的健康记录类型id获取对应的健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给健康记录类型
    if (user != ""):
        healthrecord.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给健康记录类型
    if (userid != ""):
        healthrecord.userid = userid;
    # 从request中获取记录类型信息
    name = getQuery(request, "name");
    # 如果request中存在记录类型信息，赋值给健康记录类型
    if (name != ""):
        healthrecord.name = name;
    # 从request中获取上限值信息
    shangxian = getQuery(request, "shangxian");
    # 如果request中存在上限值信息，赋值给健康记录类型
    if (shangxian != ""):
        healthrecord.shangxian = shangxian;
    # 从request中获取下限值信息
    xiaxian = getQuery(request, "xiaxian");
    # 如果request中存在下限值信息，赋值给健康记录类型
    if (xiaxian != ""):
        healthrecord.xiaxian = xiaxian;
    # 从request中获取单位信息
    danwei = getQuery(request, "danwei");
    # 如果request中存在单位信息，赋值给健康记录类型
    if (danwei != ""):
        healthrecord.danwei = danwei;

    #  调用save方法保存健康记录类型信息
    healthrecord.save();
    result['message'] = "修改健康记录类型成功"
    result['code'] = "202"

    #  返回修改健康记录类型的结果
    return HttpResponse(json.dumps(result));


#  定义删除健康记录类型方法   
def deletehealthrecordjson(request):
    result = {};

    #  使用request获取post中的健康记录类型id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除健康记录类型信息
    models.Healthrecord.objects.filter(id=id).delete();
    result['message'] = "删除健康记录类型成功"
    result['code'] = "202"

    #  返回删除健康记录类型的结果
    return HttpResponse(json.dumps(result));


#  定义搜索健康记录类型json方法，响应页面搜索请求   
def searchhealthrecordjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的健康记录类型信息
    healthrecordall = models.Healthrecord.objects.filter(user__icontains=search);

    #  返回查询结果，附带查询的健康记录类型信息
    result['healthrecordall'] = objtodic(healthrecordall)
    result['message'] = "查询健康记录类型成功"
    result['code'] = "202"

    #  返回查询健康记录类型的结果
    return HttpResponse(json.dumps(result));


#  定义搜索健康记录类型json方法，响应页面搜索请求
def usersearchhealthrecordjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");
    userid = getQuery(request, "userid");

    #  使用django的filter方法过滤查询包含search的健康记录类型信息
    healthrecordall = models.Healthrecord.objects.filter(user__icontains=search,userid=userid);

    #  返回查询结果，附带查询的健康记录类型信息
    result['healthrecordall'] = objtodic(healthrecordall)
    result['message'] = "查询健康记录类型成功"
    result['code'] = "202"

    #  返回查询健康记录类型的结果
    return HttpResponse(json.dumps(result));

#  处理健康记录类型详情json   
def healthrecorddetailsjson(request):
    result = {};

    #  使用request获取post中的健康记录类型id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取健康记录类型信息
    healthrecord = models.Healthrecord.objects.get(id=id);
    result['healthrecord'] = objtodic(healthrecord);
    result['message'] = "查询健康记录类型成功"
    result['code'] = "202"

    #  返回查询健康记录类型详情的结果
    return HttpResponse(json.dumps(result));


#  定义搜索运动类型json方法，响应页面搜索请求   
def searchmotiontypejson(request):
    result = {};

    #  获取页面post参数中的userid信息
    userid = getQuery(request, "userid");
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询
    if search:
        motionall = models.Motiontype.objects.filter(userid=userid, name__icontains=search);
    else:
        motionall = models.Motiontype.objects.filter(userid=userid);

    #  返回查询结果，附带查询的运动类型信息
    result['motionall'] = objtodic(motionall)
    result['message'] = "查询运动类型成功"
    result['code'] = "202"

    #  返回查询运动类型的结果
    return HttpResponse(json.dumps(result));
