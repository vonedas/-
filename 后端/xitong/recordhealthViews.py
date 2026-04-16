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


#    定义添加健康记录的方法，响应页面请求
def addrecordhealth(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据healthrecord,使用DJANGO all方法查询所有数据
    healthrecordall = models.Healthrecord.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加健康记录页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addrecordhealth.html', {'userall': userall, 'healthrecordall': healthrecordall, });


#  处理添加健康记录方法   
def addrecordhealthact(request):
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

    #  从页面post数据中获取健康记录类型
    healthrecordstr = request.POST.get("healthrecord");
    healthrecord = "";
    if (healthrecordstr is not None):
        healthrecord = healthrecordstr;

    #  从页面post数据中获取健康记录类型id
    healthrecordidstr = request.POST.get("healthrecordid");
    healthrecordid = "";
    if (healthrecordidstr is not None):
        healthrecordid = healthrecordidstr;

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

    #  从页面post数据中获取记录值
    valuestr = request.POST.get("value");
    value = "";
    if (valuestr is not None):
        value = valuestr;

    #  从页面post数据中获取记录时间
    recordtimestr = request.POST.get("recordtime");
    recordtime = "";
    if (recordtimestr is not None):
        recordtime = recordtimestr;

    #  将健康记录的属性赋值给健康记录，生成健康记录对象
    recordhealth = models.Recordhealth(user=user, userid=userid, healthrecord=healthrecord,
                                       healthrecordid=healthrecordid, shangxian=shangxian, xiaxian=xiaxian,
                                       danwei=danwei, value=value, recordtime=recordtime, );

    #  调用save方法保存健康记录信息
    recordhealth.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加健康记录成功,并跳转到健康记录管理页面
    return HttpResponse(u"<p>添加健康记录成功</p><a href='/recordhealth/recordhealthmanage'>返回页面</a>");


#  定义表名管理方法，响应页面recordhealthmanage请求   
def recordhealthmanage(request):
    #  通过all方法查询所有的健康记录信息
    recordhealthall = models.Recordhealth.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到健康记录管理页面，并附带所有健康记录信息
    return render(request, 'xitong/recordhealthmanage.html', {'recordhealthall': recordhealthall});


#  定义表名查看方法，响应页面recordhealthview请求   
def recordhealthview(request):
    #  通过all方法查询所有的健康记录信息
    recordhealthall = models.Recordhealth.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到健康记录查看页面，并附带所有健康记录信息
    return render(request, 'xitong/recordhealthview.html', {'recordhealthall': recordhealthall});


#  定义修改健康记录方法，通过id查询对应的健康记录信息，返回页面展示  
def updaterecordhealth(request, id):
    #  使用get方法，通过id查询对应的健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据healthrecord,使用DJANGO all方法查询所有数据
    healthrecordall = models.Healthrecord.objects.all();

    #  跳转到修改健康记录页面，并附带当前健康记录信息
    return render(request, 'xitong/updaterecordhealth.html',
                  {'recordhealth': recordhealth, 'userall': userall, 'healthrecordall': healthrecordall, });


#  定义处理修改健康记录方法   
def updaterecordhealthact(request):
    #  使用request获取post中的健康记录id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的健康记录id获取对应的健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给recordhealth的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        recordhealth.user = userstr;

    #  从页面post数据中获取用户id并赋值给recordhealth的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        recordhealth.userid = useridstr;

    #  从页面post数据中获取健康记录类型并赋值给recordhealth的healthrecord字段
    healthrecordstr = request.POST.get("healthrecord");
    if (healthrecordstr is not None):
        recordhealth.healthrecord = healthrecordstr;

    #  从页面post数据中获取健康记录类型id并赋值给recordhealth的healthrecordid字段
    healthrecordidstr = request.POST.get("healthrecordid");
    if (healthrecordidstr is not None):
        recordhealth.healthrecordid = healthrecordidstr;

    #  从页面post数据中获取上限值并赋值给recordhealth的shangxian字段
    shangxianstr = request.POST.get("shangxian");
    if (shangxianstr is not None):
        recordhealth.shangxian = shangxianstr;

    #  从页面post数据中获取下限值并赋值给recordhealth的xiaxian字段
    xiaxianstr = request.POST.get("xiaxian");
    if (xiaxianstr is not None):
        recordhealth.xiaxian = xiaxianstr;

    #  从页面post数据中获取单位并赋值给recordhealth的danwei字段
    danweistr = request.POST.get("danwei");
    if (danweistr is not None):
        recordhealth.danwei = danweistr;

    #  从页面post数据中获取记录值并赋值给recordhealth的value字段
    valuestr = request.POST.get("value");
    if (valuestr is not None):
        recordhealth.value = valuestr;

    #  从页面post数据中获取记录时间并赋值给recordhealth的recordtime字段
    recordtimestr = request.POST.get("recordtime");
    if (recordtimestr is not None):
        recordhealth.recordtime = recordtimestr;

    #  调用save方法保存健康记录信息
    recordhealth.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改健康记录成功,并跳转到健康记录管理页面
    return HttpResponse(u"<p>修改健康记录成功</p><a href='/recordhealth/recordhealthmanage'>返回页面</a>");


#  定义删除健康记录方法   
def deleterecordhealthact(request, id):
    #  调用django的delete方法，根据id删除健康记录信息
    models.Recordhealth.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除健康记录成功,并跳转到健康记录管理页面
    return HttpResponse(u"<p>删除健康记录成功</p><a href='/recordhealth/recordhealthmanage'>返回页面</a>");


#  定义搜索健康记录方法，响应页面搜索请求   
def searchrecordhealth(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的健康记录信息
    recordhealthall = models.Recordhealth.objects.filter(user__icontains=search);

    #  跳转到搜索健康记录页面，并附带查询的健康记录信息
    return render(request, 'xitong/searchrecordhealth.html', {"recordhealthall": recordhealthall});


#  处理健康记录详情   
def recordhealthdetails(request, id):
    #  根据页面传入id获取健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到健康记录详情页面,并健康记录信息传递到页面中
    return render(request, 'xitong/recordhealthdetails.html', {"recordhealth": recordhealth});


#  定义跳转user添加健康记录页面的方法  
def useraddrecordhealth(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据healthrecord,使用DJANGO all方法查询所有数据
    healthrecordall = models.Healthrecord.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加健康记录页面
    return render(request, 'xitong/useraddrecordhealth.html',
                  {'userall': userall, 'healthrecordall': healthrecordall, });


#  处理添加健康记录方法   
def useraddrecordhealthact(request):
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

    #  从页面post数据中获取健康记录类型
    healthrecordstr = request.POST.get("healthrecord");
    healthrecord = "";
    if (healthrecordstr is not None):
        healthrecord = healthrecordstr;

    #  从页面post数据中获取健康记录类型id
    healthrecordidstr = request.POST.get("healthrecordid");
    healthrecordid = "";
    if (healthrecordidstr is not None):
        healthrecordid = healthrecordidstr;

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

    #  从页面post数据中获取记录值
    valuestr = request.POST.get("value");
    value = "";
    if (valuestr is not None):
        value = valuestr;

    #  从页面post数据中获取记录时间
    recordtimestr = request.POST.get("recordtime");
    recordtime = "";
    if (recordtimestr is not None):
        recordtime = recordtimestr;

    #  将健康记录的属性赋值给健康记录，生成健康记录对象
    recordhealth = models.Recordhealth(user=user, userid=userid, healthrecord=healthrecord,
                                       healthrecordid=healthrecordid, shangxian=shangxian, xiaxian=xiaxian,
                                       danwei=danwei, value=value, recordtime=recordtime, );

    #  调用save方法保存健康记录信息
    recordhealth.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加健康记录成功,并跳转到健康记录管理页面
    return HttpResponse(u"<p>添加健康记录成功</p><a href='/recordhealth/userrecordhealthmanage'>返回页面</a>");


#  跳转user健康记录管理页面
def userrecordhealthmanage(request):
    #  查询出userid等于当前用户id的所有健康记录信息
    recordhealthall = models.Recordhealth.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回健康记录管理页面，并携带recordhealthall的数据信息
    return render(request, 'xitong/userrecordhealthmanage.html', {'recordhealthall': recordhealthall});


#  定义跳转user修改健康记录页面      
def userupdaterecordhealth(request, id):
    #  根据页面传入的健康记录id信息，查询出对应的健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据healthrecord,使用DJANGO all方法查询所有数据
    healthrecordall = models.Healthrecord.objects.all();

    #  跳转到修改健康记录页面，并携带查询出的健康记录信息
    return render(request, 'xitong/userupdaterecordhealth.html',
                  {'recordhealth': recordhealth, 'userall': userall, 'healthrecordall': healthrecordall, });


#  定义处理修改健康记录方法   
def userupdaterecordhealthact(request):
    #  使用request获取post中的健康记录id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的健康记录id获取对应的健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给recordhealth的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        recordhealth.user = userstr;

    #  从页面post数据中获取用户id并赋值给recordhealth的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        recordhealth.userid = useridstr;

    #  从页面post数据中获取健康记录类型并赋值给recordhealth的healthrecord字段
    healthrecordstr = request.POST.get("healthrecord");
    if (healthrecordstr is not None):
        recordhealth.healthrecord = healthrecordstr;

    #  从页面post数据中获取健康记录类型id并赋值给recordhealth的healthrecordid字段
    healthrecordidstr = request.POST.get("healthrecordid");
    if (healthrecordidstr is not None):
        recordhealth.healthrecordid = healthrecordidstr;

    #  从页面post数据中获取上限值并赋值给recordhealth的shangxian字段
    shangxianstr = request.POST.get("shangxian");
    if (shangxianstr is not None):
        recordhealth.shangxian = shangxianstr;

    #  从页面post数据中获取下限值并赋值给recordhealth的xiaxian字段
    xiaxianstr = request.POST.get("xiaxian");
    if (xiaxianstr is not None):
        recordhealth.xiaxian = xiaxianstr;

    #  从页面post数据中获取单位并赋值给recordhealth的danwei字段
    danweistr = request.POST.get("danwei");
    if (danweistr is not None):
        recordhealth.danwei = danweistr;

    #  从页面post数据中获取记录值并赋值给recordhealth的value字段
    valuestr = request.POST.get("value");
    if (valuestr is not None):
        recordhealth.value = valuestr;

    #  从页面post数据中获取记录时间并赋值给recordhealth的recordtime字段
    recordtimestr = request.POST.get("recordtime");
    if (recordtimestr is not None):
        recordhealth.recordtime = recordtimestr;

    #  调用save方法保存健康记录信息
    recordhealth.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改健康记录成功,并跳转到健康记录管理页面
    return HttpResponse(u"<p>修改健康记录成功</p><a href='/recordhealth/userrecordhealthmanage'>返回页面</a>");


#  定义user删除健康记录信息
def userdeleterecordhealthact(request, id):
    #  根据页面传入的健康记录id信息，删除出对应的健康记录信息
    models.Recordhealth.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除健康记录成功，并跳转到健康记录管理页面
    return HttpResponse(u"<p>删除健康记录成功</p><a href='/recordhealth/userrecordhealthmanage'>返回页面</a>");


#  处理添加健康记录Json方法
def addrecordhealthactjson(request):
    result = {};
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取健康记录类型信息
    healthrecord = getQuery(request, "healthrecord");
    # 从request中获取健康记录类型id信息
    healthrecordid = getQuery(request, "healthrecordid");
    # 从request中获取上限值信息
    shangxian = getQuery(request, "shangxian");
    # 从request中获取下限值信息
    xiaxian = getQuery(request, "xiaxian");
    # 从request中获取单位信息
    danwei = getQuery(request, "danwei");
    # 从request中获取记录值信息
    value = getQuery(request, "value");
    # 从request中获取记录时间信息
    recordtime = getQuery(request, "recordtime");

    #  将健康记录的属性赋值给健康记录，生成健康记录对象
    recordhealth = models.Recordhealth(user=user, userid=userid, healthrecord=healthrecord,
                                       healthrecordid=healthrecordid, shangxian=shangxian, xiaxian=xiaxian,
                                       danwei=danwei, value=value, recordtime=recordtime, );

    #  调用save方法保存健康记录信息
    recordhealth.save();
    result['message'] = "添加健康记录成功"
    result['code'] = "202"

    #  返回添加健康记录的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改健康记录方法   
def updaterecordhealthactjson(request):
    result = {};

    #  使用request获取post中的健康记录id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的健康记录id获取对应的健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给健康记录
    if (user != ""):
        recordhealth.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给健康记录
    if (userid != ""):
        recordhealth.userid = userid;
    # 从request中获取健康记录类型信息
    healthrecord = getQuery(request, "healthrecord");
    # 如果request中存在健康记录类型信息，赋值给健康记录
    if (healthrecord != ""):
        recordhealth.healthrecord = healthrecord;
    # 从request中获取健康记录类型id信息
    healthrecordid = getQuery(request, "healthrecordid");
    # 如果request中存在健康记录类型id信息，赋值给健康记录
    if (healthrecordid != ""):
        recordhealth.healthrecordid = healthrecordid;
    # 从request中获取上限值信息
    shangxian = getQuery(request, "shangxian");
    # 如果request中存在上限值信息，赋值给健康记录
    if (shangxian != ""):
        recordhealth.shangxian = shangxian;
    # 从request中获取下限值信息
    xiaxian = getQuery(request, "xiaxian");
    # 如果request中存在下限值信息，赋值给健康记录
    if (xiaxian != ""):
        recordhealth.xiaxian = xiaxian;
    # 从request中获取单位信息
    danwei = getQuery(request, "danwei");
    # 如果request中存在单位信息，赋值给健康记录
    if (danwei != ""):
        recordhealth.danwei = danwei;
    # 从request中获取记录值信息
    value = getQuery(request, "value");
    # 如果request中存在记录值信息，赋值给健康记录
    if (value != ""):
        recordhealth.value = value;
    # 从request中获取记录时间信息
    recordtime = getQuery(request, "recordtime");
    # 如果request中存在记录时间信息，赋值给健康记录
    if (recordtime != ""):
        recordhealth.recordtime = recordtime;

    #  调用save方法保存健康记录信息
    recordhealth.save();
    result['message'] = "修改健康记录成功"
    result['code'] = "202"

    #  返回修改健康记录的结果
    return HttpResponse(json.dumps(result));


#  定义删除健康记录方法   
def deleterecordhealthjson(request):
    result = {};

    #  使用request获取post中的健康记录id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除健康记录信息
    models.Recordhealth.objects.filter(id=id).delete();
    result['message'] = "删除健康记录成功"
    result['code'] = "202"

    #  返回删除健康记录的结果
    return HttpResponse(json.dumps(result));


#  定义搜索健康记录json方法，响应页面搜索请求   
def searchrecordhealthjson(request):
    result = {};
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");

    # 使用django的filter方法过滤查询该用户的健康记录信息   
    recordhealthall = models.Recordhealth.objects.filter(userid=userid);

    # 返回查询结果
    result['recordhealthall'] = objtodic(recordhealthall);
    result['message'] = "查询健康记录成功";
    result['code'] = "202";

    # 返回查询结果
    return HttpResponse(json.dumps(result));


#  处理健康记录详情   
def recordhealthdetailsjson(request):
    result = {};

    #  使用request获取post中的健康记录id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取健康记录信息
    recordhealth = models.Recordhealth.objects.get(id=id);
    result['recordhealth'] = objtodic(recordhealth);
    result['message'] = "查询健康记录成功"
    result['code'] = "202"

    #  返回查询健康记录详情的结果
    return HttpResponse(json.dumps(result));


#  定义获取健康记录类型列表方法
def getHealthRecords(request):
    result = {};
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");

    # 查询系统预设和用户自定义的健康记录类型
    healthrecordall = models.Healthrecord.objects.filter(userid__in=[0, int(userid)]);

    # 返回查询结果
    result['healthrecordall'] = objtodic(healthrecordall);
    result['message'] = "获取健康记录类型成功";
    result['code'] = "202";

    # 返回查询结果
    return HttpResponse(json.dumps(result));


# 定义获取健康记录可视化数据的方法
def getHealthRecordVisualizationData(request):
    result = {}

    # 从request中获取参数
    userid = getQuery(request, "userid")
    healthrecordid = getQuery(request, "healthrecordid")
    days = int(getQuery(request, "days") or 7)  # 默认7天

    # 获取当前时间
    import datetime
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=days)

    # 构建查询条件
    query = {
        'userid': userid
    }

    # 如果选择了特定的健康记录类型，添加到查询条件
    if healthrecordid:
        query['healthrecordid'] = healthrecordid

    # 查询数据
    records = models.Recordhealth.objects.filter(**query).order_by('recordtime')

    # 过滤日期范围
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    filtered_records = []
    for record in records:
        record_date = record.recordtime.split(' ')[0]  # 只取日期部分
        if start_date_str <= record_date <= end_date_str:
            filtered_records.append(record)

    # 转换数据为前端需要的格
    records_data = []
    for record in filtered_records:
        records_data.append({
            'id': record.id,
            'value': float(record.value),
            'recordtime': record.recordtime,
            'healthrecord': record.healthrecord,
            'danwei': record.danwei,
            'shangxian': float(record.shangxian) if record.shangxian else None,
            'xiaxian': float(record.xiaxian) if record.xiaxian else None
        })

    # 返回数据
    result['records'] = records_data
    result['message'] = "获取健康记录可视化数据成功"
    result['code'] = "202"

    return HttpResponse(json.dumps(result))


# 获取每日摄入/消耗卡路里趋势（仅近7/30日，合计同一天数据）
def getCaloriesTrendSimple(request):
    import datetime
    result = {}

    userid = getQuery(request, "userid")
    days = int(getQuery(request, "days") or 30)
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=days-1)

    # 生成日期列表
    date_list = [(start_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]

    # 查询饮食记录
    yinshilogs = models.Yinshilog.objects.filter(userid=userid, shijian__gte=start_date.strftime('%Y-%m-%d'), shijian__lte=end_date.strftime('%Y-%m-%d'))
    yinshi_dict = {}
    for log in yinshilogs:
        date = log.shijian
        kaluli = float(log.kaluli) if log.kaluli else 0
        yinshi_dict[date] = yinshi_dict.get(date, 0) + kaluli

    # 查询锻炼记录
    duanlianlogs = models.Duanlianlog.objects.filter(userid=userid, shijian__gte=start_date.strftime('%Y-%m-%d'), shijian__lte=end_date.strftime('%Y-%m-%d'))
    duanlian_dict = {}
    for log in duanlianlogs:
        date = log.shijian
        kaluli = float(log.kaluli) if log.kaluli else 0
        duanlian_dict[date] = duanlian_dict.get(date, 0) + kaluli

    # 组装结果
    calories_in = []
    calories_out = []
    for date in date_list:
        calories_in.append({'date': date, 'value': yinshi_dict.get(date, 0)})
        calories_out.append({'date': date, 'value': duanlian_dict.get(date, 0)})

    result['calories_in'] = calories_in
    result['calories_out'] = calories_out
    result['message'] = "获取卡路里趋势成功"
    result['code'] = "202"
    return HttpResponse(json.dumps(result))
