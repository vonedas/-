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


#    定义添加绑定的方法，响应页面请求
def addbangding(request):
    #  获取页面数据zinv,使用DJANGO all方法查询所有数据
    zinvall = models.Zinv.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加绑定页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addbangding.html', {'zinvall': zinvall, 'userall': userall, });


#  处理添加绑定方法   
def addbangdingact(request):
    #  从页面post数据中获取子女
    zinvstr = request.POST.get("zinv");
    zinv = "";
    if (zinvstr is not None):
        zinv = zinvstr;

    #  从页面post数据中获取子女id
    zinvidstr = request.POST.get("zinvid");
    zinvid = "";
    if (zinvidstr is not None):
        zinvid = zinvidstr;

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

    #  将绑定的属性赋值给绑定，生成绑定对象
    bangding = models.Bangding(zinv=zinv, zinvid=zinvid, user=user, userid=userid, );

    #  调用save方法保存绑定信息
    bangding.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加绑定成功,并跳转到绑定管理页面
    return HttpResponse(u"<p>添加绑定成功</p><a href='/bangding/bangdingmanage'>返回页面</a>");


#  定义表名管理方法，响应页面bangdingmanage请求   
def bangdingmanage(request):
    #  通过all方法查询所有的绑定信息
    bangdingall = models.Bangding.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到绑定管理页面，并附带所有绑定信息
    return render(request, 'xitong/bangdingmanage.html', {'bangdingall': bangdingall});


#  定义表名查看方法，响应页面bangdingview请求   
def bangdingview(request):
    #  通过all方法查询所有的绑定信息
    bangdingall = models.Bangding.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到绑定查看页面，并附带所有绑定信息
    return render(request, 'xitong/bangdingview.html', {'bangdingall': bangdingall});


#  定义修改绑定方法，通过id查询对应的绑定信息，返回页面展示  
def updatebangding(request, id):
    #  使用get方法，通过id查询对应的绑定信息
    bangding = models.Bangding.objects.get(id=id);

    #  获取页面数据zinv,使用DJANGO all方法查询所有数据
    zinvall = models.Zinv.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改绑定页面，并附带当前绑定信息
    return render(request, 'xitong/updatebangding.html',
                  {'bangding': bangding, 'zinvall': zinvall, 'userall': userall, });


#  定义处理修改绑定方法   
def updatebangdingact(request):
    #  使用request获取post中的绑定id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的绑定id获取对应的绑定信息
    bangding = models.Bangding.objects.get(id=id);

    #  从页面post数据中获取子女并赋值给bangding的zinv字段
    zinvstr = request.POST.get("zinv");
    if (zinvstr is not None):
        bangding.zinv = zinvstr;

    #  从页面post数据中获取子女id并赋值给bangding的zinvid字段
    zinvidstr = request.POST.get("zinvid");
    if (zinvidstr is not None):
        bangding.zinvid = zinvidstr;

    #  从页面post数据中获取用户并赋值给bangding的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        bangding.user = userstr;

    #  从页面post数据中获取用户id并赋值给bangding的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        bangding.userid = useridstr;

    #  调用save方法保存绑定信息
    bangding.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改绑定成功,并跳转到绑定管理页面
    return HttpResponse(u"<p>修改绑定成功</p><a href='/bangding/bangdingmanage'>返回页面</a>");


#  定义删除绑定方法   
def deletebangdingact(request, id):
    #  调用django的delete方法，根据id删除绑定信息
    models.Bangding.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除绑定成功,并跳转到绑定管理页面
    return HttpResponse(u"<p>删除绑定成功</p><a href='/bangding/bangdingmanage'>返回页面</a>");


#  定义搜索绑定方法，响应页面搜索请求   
def searchbangding(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的绑定信息
    bangdingall = models.Bangding.objects.filter(zinv__icontains=search);

    #  跳转到搜索绑定页面，并附带查询的绑定信息
    return render(request, 'xitong/searchbangding.html', {"bangdingall": bangdingall});


#  处理绑定详情   
def bangdingdetails(request, id):
    #  根据页面传入id获取绑定信息
    bangding = models.Bangding.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到绑定详情页面,并绑定信息传递到页面中
    return render(request, 'xitong/bangdingdetails.html', {"bangding": bangding});


#  定义跳转zinv添加绑定页面的方法  
def zinvaddbangding(request):
    #  获取页面数据zinv,使用DJANGO all方法查询所有数据
    zinvall = models.Zinv.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回zinv添加绑定页面
    return render(request, 'xitong/zinvaddbangding.html', {'zinvall': zinvall, 'userall': userall, });


#  处理添加绑定方法   
def zinvaddbangdingact(request):
    #  从页面post数据中获取子女
    zinvstr = request.POST.get("zinv");
    zinv = "";
    if (zinvstr is not None):
        zinv = zinvstr;

    #  从页面post数据中获取子女id
    zinvidstr = request.POST.get("zinvid");
    zinvid = "";
    if (zinvidstr is not None):
        zinvid = zinvidstr;

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

    #  将绑定的属性赋值给绑定，生成绑定对象
    bangding = models.Bangding(zinv=zinv, zinvid=zinvid, user=user, userid=userid, );

    #  调用save方法保存绑定信息
    bangding.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加绑定成功,并跳转到绑定管理页面
    return HttpResponse(u"<p>添加绑定成功</p><a href='/bangding/zinvbangdingmanage'>返回页面</a>");


#  跳转zinv绑定管理页面
def zinvbangdingmanage(request):
    #  查询出zinvid等于当前用户id的所有绑定信息
    bangdingall = models.Bangding.objects.filter(zinvid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回绑定管理页面，并携带bangdingall的数据信息
    return render(request, 'xitong/zinvbangdingmanage.html', {'bangdingall': bangdingall});


#  定义跳转zinv修改绑定页面      
def zinvupdatebangding(request, id):
    #  根据页面传入的绑定id信息，查询出对应的绑定信息
    bangding = models.Bangding.objects.get(id=id);

    #  获取页面数据zinv,使用DJANGO all方法查询所有数据
    zinvall = models.Zinv.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改绑定页面，并携带查询出的绑定信息
    return render(request, 'xitong/zinvupdatebangding.html',
                  {'bangding': bangding, 'zinvall': zinvall, 'userall': userall, });


#  定义处理修改绑定方法   
def zinvupdatebangdingact(request):
    #  使用request获取post中的绑定id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的绑定id获取对应的绑定信息
    bangding = models.Bangding.objects.get(id=id);

    #  从页面post数据中获取子女并赋值给bangding的zinv字段
    zinvstr = request.POST.get("zinv");
    if (zinvstr is not None):
        bangding.zinv = zinvstr;

    #  从页面post数据中获取子女id并赋值给bangding的zinvid字段
    zinvidstr = request.POST.get("zinvid");
    if (zinvidstr is not None):
        bangding.zinvid = zinvidstr;

    #  从页面post数据中获取用户并赋值给bangding的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        bangding.user = userstr;

    #  从页面post数据中获取用户id并赋值给bangding的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        bangding.userid = useridstr;

    #  调用save方法保存绑定信息
    bangding.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改绑定成功,并跳转到绑定管理页面
    return HttpResponse(u"<p>修改绑定成功</p><a href='/bangding/zinvbangdingmanage'>返回页面</a>");


#  定义zinv删除绑定信息
def zinvdeletebangdingact(request, id):
    #  根据页面传入的绑定id信息，删除出对应的绑定信息
    models.Bangding.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除绑定成功，并跳转到绑定管理页面
    return HttpResponse(u"<p>删除绑定成功</p><a href='/bangding/zinvbangdingmanage'>返回页面</a>");


#  处理添加绑定Json方法
def addbangdingactjson(request):
    result = {};
    # 从request中获取子女信息
    zinv = getQuery(request, "zinv");
    # 从request中获取子女id信息
    zinvid = getQuery(request, "zinvid");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");

    #  将绑定的属性赋值给绑定，生成绑定对象
    bangding = models.Bangding(zinv=zinv, zinvid=zinvid, user=user, userid=userid, );

    #  调用save方法保存绑定信息
    bangding.save();
    result['message'] = "添加绑定成功"
    result['code'] = "202"

    #  返回添加绑定的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改绑定方法   
def updatebangdingactjson(request):
    result = {};

    #  使用request获取post中的绑定id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的绑定id获取对应的绑定信息
    bangding = models.Bangding.objects.get(id=id);
    # 从request中获取子女信息
    zinv = getQuery(request, "zinv");
    # 如果request中存在子女信息，赋值给绑定
    if (zinv != ""):
        bangding.zinv = zinv;
    # 从request中获取子女id信息
    zinvid = getQuery(request, "zinvid");
    # 如果request中存在子女id信息，赋值给绑定
    if (zinvid != ""):
        bangding.zinvid = zinvid;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给绑定
    if (user != ""):
        bangding.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给绑定
    if (userid != ""):
        bangding.userid = userid;

    #  调用save方法保存绑定信息
    bangding.save();
    result['message'] = "修改绑定成功"
    result['code'] = "202"

    #  返回修改绑定的结果
    return HttpResponse(json.dumps(result));


#  定义删除绑定方法   
def deletebangdingjson(request):
    result = {};

    #  使用request获取post中的绑定id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除绑定信息
    models.Bangding.objects.filter(id=id).delete();
    result['message'] = "删除绑定成功"
    result['code'] = "202"

    #  返回删除绑定的结果
    return HttpResponse(json.dumps(result));


#  定义搜索绑定json方法，响应页面搜索请求   
def searchbangdingjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的绑定信息
    bangdingall = models.Bangding.objects.filter(zinv__icontains=search);

    #  返回查询结果，附带查询的绑定信息
    result['bangdingall'] = objtodic(bangdingall)
    result['message'] = "查询绑定成功"
    result['code'] = "202"

    #  返回查询绑定的结果
    return HttpResponse(json.dumps(result));


#  处理绑定详情   
def bangdingdetailsjson(request):
    result = {};

    #  使用request获取post中的绑定id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取绑定信息
    bangding = models.Bangding.objects.get(id=id);
    result['bangding'] = objtodic(bangding);
    result['message'] = "查询绑定成功"
    result['code'] = "202"

    #  返回查询绑定详情的结果
    return HttpResponse(json.dumps(result));
