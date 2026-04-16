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


#    定义添加血压的方法，响应页面请求
def addxueya(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加血压页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addxueya.html', {'userall': userall, });


#  处理添加血压方法   
def addxueyaact(request):
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

    #  从页面post数据中获取数值
    shuzhistr = request.POST.get("shuzhi");
    shuzhi = "";
    if (shuzhistr is not None):
        shuzhi = shuzhistr;

    #  从页面post数据中获取类型
    leixingstr = request.POST.get("leixing");
    leixing = "";
    if (leixingstr is not None):
        leixing = leixingstr;

    #  从页面post数据中获取时间
    shijianstr = request.POST.get("shijian");
    shijian = "";
    if (shijianstr is not None):
        shijian = shijianstr;

    #  将血压的属性赋值给血压，生成血压对象
    xueya = models.Xueya(user=user, userid=userid, shuzhi=shuzhi, leixing=leixing, shijian=shijian, );

    #  调用save方法保存血压信息
    xueya.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加血压成功,并跳转到血压管理页面
    return HttpResponse(u"<p>添加血压成功</p><a href='/xueya/xueyamanage'>返回页面</a>");


#  定义表名管理方法，响应页面xueyamanage请求   
def xueyamanage(request):
    #  通过all方法查询所有的血压信息
    xueyaall = models.Xueya.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到血压管理页面，并附带所有血压信息
    return render(request, 'xitong/xueyamanage.html', {'xueyaall': xueyaall});


#  定义表名查看方法，响应页面xueyaview请求   
def xueyaview(request):
    #  通过all方法查询所有的血压信息
    xueyaall = models.Xueya.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到血压查看页面，并附带所有血压信息
    return render(request, 'xitong/xueyaview.html', {'xueyaall': xueyaall});


#  定义修改血压方法，通过id查询对应的血压信息，返回页面展示  
def updatexueya(request, id):
    #  使用get方法，通过id查询对应的血压信息
    xueya = models.Xueya.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改血压页面，并附带当前血压信息
    return render(request, 'xitong/updatexueya.html', {'xueya': xueya, 'userall': userall, });


#  定义处理修改血压方法   
def updatexueyaact(request):
    #  使用request获取post中的血压id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的血压id获取对应的血压信息
    xueya = models.Xueya.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给xueya的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        xueya.user = userstr;

    #  从页面post数据中获取用户id并赋值给xueya的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        xueya.userid = useridstr;

    #  从页面post数据中获取数值并赋值给xueya的shuzhi字段
    shuzhistr = request.POST.get("shuzhi");
    if (shuzhistr is not None):
        xueya.shuzhi = shuzhistr;

    #  从页面post数据中获取类型并赋值给xueya的leixing字段
    leixingstr = request.POST.get("leixing");
    if (leixingstr is not None):
        xueya.leixing = leixingstr;

    #  从页面post数据中获取时间并赋值给xueya的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        xueya.shijian = shijianstr;

    #  调用save方法保存血压信息
    xueya.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改血压成功,并跳转到血压管理页面
    return HttpResponse(u"<p>修改血压成功</p><a href='/xueya/xueyamanage'>返回页面</a>");


#  定义删除血压方法   
def deletexueyaact(request, id):
    #  调用django的delete方法，根据id删除血压信息
    models.Xueya.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除血压成功,并跳转到血压管理页面
    return HttpResponse(u"<p>删除血压成功</p><a href='/xueya/xueyamanage'>返回页面</a>");


#  定义搜索血压方法，响应页面搜索请求   
def searchxueya(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的血压信息
    xueyaall = models.Xueya.objects.filter(user__icontains=search);

    #  跳转到搜索血压页面，并附带查询的血压信息
    return render(request, 'xitong/searchxueya.html', {"xueyaall": xueyaall});


#  处理血压详情   
def xueyadetails(request, id):
    #  根据页面传入id获取血压信息
    xueya = models.Xueya.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到血压详情页面,并血压信息传递到页面中
    return render(request, 'xitong/xueyadetails.html', {"xueya": xueya});


#  定义跳转user添加血压页面的方法  
def useraddxueya(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加血压页面
    return render(request, 'xitong/useraddxueya.html', {'userall': userall, });


#  处理添加血压方法   
def useraddxueyaact(request):
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

    #  从页面post数据中获取数值
    shuzhistr = request.POST.get("shuzhi");
    shuzhi = "";
    if (shuzhistr is not None):
        shuzhi = shuzhistr;

    #  从页面post数据中获取类型
    leixingstr = request.POST.get("leixing");
    leixing = "";
    if (leixingstr is not None):
        leixing = leixingstr;

    #  从页面post数据中获取时间
    shijianstr = request.POST.get("shijian");
    shijian = "";
    if (shijianstr is not None):
        shijian = shijianstr;

    #  将血压的属性赋值给血压，生成血压对象
    xueya = models.Xueya(user=user, userid=userid, shuzhi=shuzhi, leixing=leixing, shijian=shijian, );

    #  调用save方法保存血压信息
    xueya.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加血压成功,并跳转到血压管理页面
    return HttpResponse(u"<p>添加血压成功</p><a href='/xueya/userxueyamanage'>返回页面</a>");


#  跳转user血压管理页面
def userxueyamanage(request):
    #  查询出userid等于当前用户id的所有血压信息
    xueyaall = models.Xueya.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回血压管理页面，并携带xueyaall的数据信息
    return render(request, 'xitong/userxueyamanage.html', {'xueyaall': xueyaall});


#  定义跳转user修改血压页面      
def userupdatexueya(request, id):
    #  根据页面传入的血压id信息，查询出对应的血压信息
    xueya = models.Xueya.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改血压页面，并携带查询出的血压信息
    return render(request, 'xitong/userupdatexueya.html', {'xueya': xueya, 'userall': userall, });


#  定义处理修改血压方法   
def userupdatexueyaact(request):
    #  使用request获取post中的血压id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的血压id获取对应的血压信息
    xueya = models.Xueya.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给xueya的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        xueya.user = userstr;

    #  从页面post数据中获取用户id并赋值给xueya的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        xueya.userid = useridstr;

    #  从页面post数据中获取数值并赋值给xueya的shuzhi字段
    shuzhistr = request.POST.get("shuzhi");
    if (shuzhistr is not None):
        xueya.shuzhi = shuzhistr;

    #  从页面post数据中获取类型并赋值给xueya的leixing字段
    leixingstr = request.POST.get("leixing");
    if (leixingstr is not None):
        xueya.leixing = leixingstr;

    #  从页面post数据中获取时间并赋值给xueya的shijian字段
    shijianstr = request.POST.get("shijian");
    if (shijianstr is not None):
        xueya.shijian = shijianstr;

    #  调用save方法保存血压信息
    xueya.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改血压成功,并跳转到血压管理页面
    return HttpResponse(u"<p>修改血压成功</p><a href='/xueya/userxueyamanage'>返回页面</a>");


#  定义user删除血压信息
def userdeletexueyaact(request, id):
    #  根据页面传入的血压id信息，删除出对应的血压信息
    models.Xueya.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除血压成功，并跳转到血压管理页面
    return HttpResponse(u"<p>删除血压成功</p><a href='/xueya/userxueyamanage'>返回页面</a>");


#  处理添加血压Json方法
def addxueyaactjson(request):
    result = {};
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取数值信息
    shuzhi = getQuery(request, "shuzhi");
    # 从request中获取类型信息
    leixing = getQuery(request, "leixing");
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");

    #  将血压的属性赋值给血压，生成血压对象
    xueya = models.Xueya(user=user, userid=userid, shuzhi=shuzhi, leixing=leixing, shijian=shijian, );

    #  调用save方法保存血压信息
    xueya.save();
    result['message'] = "添加血压成功"
    result['code'] = "202"

    #  返回添加血压的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改血压方法   
def updatexueyaactjson(request):
    result = {};

    #  使用request获取post中的血压id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的血压id获取对应的血压信息
    xueya = models.Xueya.objects.get(id=id);
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给血压
    if (user != ""):
        xueya.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给血压
    if (userid != ""):
        xueya.userid = userid;
    # 从request中获取数值信息
    shuzhi = getQuery(request, "shuzhi");
    # 如果request中存在数值信息，赋值给血压
    if (shuzhi != ""):
        xueya.shuzhi = shuzhi;
    # 从request中获取类型信息
    leixing = getQuery(request, "leixing");
    # 如果request中存在类型信息，赋值给血压
    if (leixing != ""):
        xueya.leixing = leixing;
    # 从request中获取时间信息
    shijian = getQuery(request, "shijian");
    # 如果request中存在时间信息，赋值给血压
    if (shijian != ""):
        xueya.shijian = shijian;

    #  调用save方法保存血压信息
    xueya.save();
    result['message'] = "修改血压成功"
    result['code'] = "202"

    #  返回修改血压的结果
    return HttpResponse(json.dumps(result));


#  定义删除血压方法   
def deletexueyajson(request):
    result = {};

    #  使用request获取post中的血压id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除血压信息
    models.Xueya.objects.filter(id=id).delete();
    result['message'] = "删除血压成功"
    result['code'] = "202"

    #  返回删除血压的结果
    return HttpResponse(json.dumps(result));


#  定义搜索血压json方法，响应页面搜索请求   
def searchxueyajson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的血压信息
    xueyaall = models.Xueya.objects.filter(user__icontains=search);

    #  返回查询结果，附带查询的血压信息
    result['xueyaall'] = objtodic(xueyaall)
    result['message'] = "查询血压成功"
    result['code'] = "202"

    #  返回查询血压的结果
    return HttpResponse(json.dumps(result));


#  处理血压详情   
def xueyadetailsjson(request):
    result = {};

    #  使用request获取post中的血压id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取血压信息
    xueya = models.Xueya.objects.get(id=id);
    result['xueya'] = objtodic(xueya);
    result['message'] = "查询血压成功"
    result['code'] = "202"

    #  返回查询血压详情的结果
    return HttpResponse(json.dumps(result));
