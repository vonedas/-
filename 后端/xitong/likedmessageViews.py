#coding:utf-8
from django.db.models import QuerySet
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse
from . import models
import random,os,json;



#  定义上传文件方法      
def uploadFile(request,filename):

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

#定义获取数据方法
def getQuery(request,name):
    #定义返回数据初始值
    result = "";

    #尝试从GET参数中获取数据
    if(request.GET.get(name) is not None):
        #如果GET中存在数据，则返回GET中的数据信息
        result = request.GET.get(name);
    #尝试从POST参数中获取数据
    elif(request.POST.get(name) is not None):
        #如果POST中存在数据，则返回POST中的数据信息
        result = request.POST.get(name);
    else:
        #从request的body中获取数据
        try:
            json_str = request.body  # 属性获取最原始的请求体数据
            json_dict = json.loads(json_str)  # 将原始数据转成字典格式
            result = json_dict.get(name)  # 获取数据
        except:
            pass;

    #返回数据信息
    return result;

# 将Django的模型对象转换为字典信息
def objtodic(obj):
    # 如果obj是QuerySet类，则遍历转换
    if(type(obj) == QuerySet):
        result = [];
        # 进行遍历并转换对象为字典
        for i in obj:
            result.append(i.todic())

        # 返回转换结果
        return result;
    else:
        # 返回转换结果
        return obj.todic();




#    定义添加点赞通知的方法，响应页面请求
def addlikedmessage(request):

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  返回添加点赞通知页面，并将该页面数据传递到视图中   
    return  render(request,'xitong/addlikedmessage.html',{});


#  处理添加点赞通知方法   
def addlikedmessageact(request):

#  从页面post数据中获取被点赞用户   
    likeduserstr = request.POST.get("likeduser");
    likeduser = "";
    if(likeduserstr is not None):
        likeduser = likeduserstr;

#  从页面post数据中获取被点赞用户id   
    likeduseridstr = request.POST.get("likeduserid");
    likeduserid = "";
    if(likeduseridstr is not None):
        likeduserid = likeduseridstr;

#  从页面post数据中获取用户   
    userstr = request.POST.get("user");
    user = "";
    if(userstr is not None):
        user = userstr;

#  从页面post数据中获取用户id   
    useridstr = request.POST.get("userid");
    userid = "";
    if(useridstr is not None):
        userid = useridstr;

#  从页面post数据中获取是否已读   
    isreadstr = request.POST.get("isread");
    isread = "";
    if(isreadstr is not None):
        isread = isreadstr;

#  将点赞通知的属性赋值给点赞通知，生成点赞通知对象   
    likedmessage = models.Likedmessage(likeduser=likeduser,likeduserid=likeduserid,user=user,userid=userid,isread=isread,);

#  调用save方法保存点赞通知信息   
    likedmessage.save();

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  返回页面提示信息,添加点赞通知成功,并跳转到点赞通知管理页面   
    return HttpResponse(u"<p>添加点赞通知成功</p><a href='/likedmessage/likedmessagemanage'>返回页面</a>");


#  定义表名管理方法，响应页面likedmessagemanage请求   
def likedmessagemanage(request):

#  通过all方法查询所有的点赞通知信息   
    likedmessageall = models.Likedmessage.objects.all()

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  跳转到点赞通知管理页面，并附带所有点赞通知信息   
    return  render(request,'xitong/likedmessagemanage.html',{'likedmessageall':likedmessageall});


#  定义表名查看方法，响应页面likedmessageview请求   
def likedmessageview(request):

#  通过all方法查询所有的点赞通知信息   
    likedmessageall = models.Likedmessage.objects.all()

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  跳转到点赞通知查看页面，并附带所有点赞通知信息   
    return  render(request,'xitong/likedmessageview.html',{'likedmessageall':likedmessageall});


#  定义修改点赞通知方法，通过id查询对应的点赞通知信息，返回页面展示  
def updatelikedmessage(request,id):

#  使用get方法，通过id查询对应的点赞通知信息  
    likedmessage = models.Likedmessage.objects.get(id=id);


#  跳转到修改点赞通知页面，并附带当前点赞通知信息   
    return render(request, 'xitong/updatelikedmessage.html', {'likedmessage': likedmessage,});


#  定义处理修改点赞通知方法   
def updatelikedmessageact(request):

#  使用request获取post中的点赞通知id参数   
    id = request.POST.get("id");

#  使用model的get方法根据页面传入的点赞通知id获取对应的点赞通知信息   
    likedmessage = models.Likedmessage.objects.get(id=id);

#  从页面post数据中获取被点赞用户并赋值给likedmessage的likeduser字段   
    likeduserstr = request.POST.get("likeduser");
    if(likeduserstr is not None):
        likedmessage.likeduser = likeduserstr;

#  从页面post数据中获取被点赞用户id并赋值给likedmessage的likeduserid字段   
    likeduseridstr = request.POST.get("likeduserid");
    if(likeduseridstr is not None):
        likedmessage.likeduserid = likeduseridstr;

#  从页面post数据中获取用户并赋值给likedmessage的user字段   
    userstr = request.POST.get("user");
    if(userstr is not None):
        likedmessage.user = userstr;

#  从页面post数据中获取用户id并赋值给likedmessage的userid字段   
    useridstr = request.POST.get("userid");
    if(useridstr is not None):
        likedmessage.userid = useridstr;

#  从页面post数据中获取是否已读并赋值给likedmessage的isread字段   
    isreadstr = request.POST.get("isread");
    if(isreadstr is not None):
        likedmessage.isread = isreadstr;

#  调用save方法保存点赞通知信息   
    likedmessage.save();

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  返回页面提示信息,修改点赞通知成功,并跳转到点赞通知管理页面   
    return HttpResponse(u"<p>修改点赞通知成功</p><a href='/likedmessage/likedmessagemanage'>返回页面</a>");


#  定义删除点赞通知方法   
def deletelikedmessageact(request,id):

#  调用django的delete方法，根据id删除点赞通知信息   
    models.Likedmessage.objects.filter(id=id).delete();

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  返回页面提示信息,删除点赞通知成功,并跳转到点赞通知管理页面   
    return HttpResponse(u"<p>删除点赞通知成功</p><a href='/likedmessage/likedmessagemanage'>返回页面</a>");


#  定义搜索点赞通知方法，响应页面搜索请求   
def searchlikedmessage(request):

#  获取页面post参数中的search信息   
    search = request.POST.get("search");

#  如果search为None   
    if(search is None):

#  设置search等于空字符串   
        search = "";

#  使用django的filter方法过滤查询包含search的点赞通知信息   
    likedmessageall = models.Likedmessage.objects.filter(likeduser__icontains=search);

#  跳转到搜索点赞通知页面，并附带查询的点赞通知信息   
    return render(request, 'xitong/searchlikedmessage.html', {"likedmessageall": likedmessageall});


#  处理点赞通知详情   
def likedmessagedetails(request,id):

#  根据页面传入id获取点赞通知信息   
    likedmessage = models.Likedmessage.objects.get(id=id);

#  获取页面数据中的backurl参数   
    backurl = request.POST.get("backurl");

#  如果backurl不等于none   
    if(backurl is not None):

#  返回操作成功，并跳转到backurl链接处   
        return HttpResponse(u"<p>操作成功</p><a href='"+ backurl +u"'>返回页面</a>");

#  跳转到点赞通知详情页面,并点赞通知信息传递到页面中   
    return render(request, 'xitong/likedmessagedetails.html', {"likedmessage": likedmessage});








#  处理添加点赞通知Json方法   
def addlikedmessageactjson(request):
    result = {};
    # 从request中获取被点赞用户信息
    likeduser = getQuery(request,"likeduser");
    # 从request中获取被点赞用户id信息
    likeduserid = getQuery(request,"likeduserid");
    # 从request中获取用户信息
    user = getQuery(request,"user");
    # 从request中获取用户id信息
    userid = getQuery(request,"userid");
    # 从request中获取是否已读信息
    isread = getQuery(request,"isread");

#  将点赞通知的属性赋值给点赞通知，生成点赞通知对象   
    likedmessage = models.Likedmessage(likeduser=likeduser,likeduserid=likeduserid,user=user,userid=userid,isread=isread,);

#  调用save方法保存点赞通知信息   
    likedmessage.save();
    result['message'] = "添加点赞通知成功"
    result['code'] = "202"

#  返回添加点赞通知的结果   
    return HttpResponse(json.dumps(result));


#  定义处理修改点赞通知方法   
def updatelikedmessageactjson(request):
    result = {};

#  使用request获取post中的点赞通知id参数   
    id = getQuery(request,"id");

#  使用model的get方法根据页面传入的点赞通知id获取对应的点赞通知信息   
    likedmessage = models.Likedmessage.objects.get(id=id);
    # 从request中获取被点赞用户信息
    likeduser = getQuery(request,"likeduser");
    # 如果request中存在被点赞用户信息，赋值给点赞通知
    if(likeduser != ""):
        likedmessage.likeduser = likeduser;
    # 从request中获取被点赞用户id信息
    likeduserid = getQuery(request,"likeduserid");
    # 如果request中存在被点赞用户id信息，赋值给点赞通知
    if(likeduserid != ""):
        likedmessage.likeduserid = likeduserid;
    # 从request中获取用户信息
    user = getQuery(request,"user");
    # 如果request中存在用户信息，赋值给点赞通知
    if(user != ""):
        likedmessage.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request,"userid");
    # 如果request中存在用户id信息，赋值给点赞通知
    if(userid != ""):
        likedmessage.userid = userid;
    # 从request中获取是否已读信息
    isread = getQuery(request,"isread");
    # 如果request中存在是否已读信息，赋值给点赞通知
    if(isread != ""):
        likedmessage.isread = isread;

#  调用save方法保存点赞通知信息   
    likedmessage.save();
    result['message'] = "修改点赞通知成功"
    result['code'] = "202"

#  返回修改点赞通知的结果   
    return HttpResponse(json.dumps(result));


#  定义删除点赞通知方法   
def deletelikedmessagejson(request):
    result = {};

#  使用request获取post中的点赞通知id参数   
    id = getQuery(request,"id");

#  调用django的delete方法，根据id删除点赞通知信息   
    models.Likedmessage.objects.filter(id=id).delete();
    result['message'] = "删除点赞通知成功"
    result['code'] = "202"

#  返回删除点赞通知的结果   
    return HttpResponse(json.dumps(result));


#  定义搜索点赞通知json方法，响应页面搜索请求   
def searchlikedmessagejson(request):
    result = {};

#  获取页面post参数中的search信息   
    search = getQuery(request,"search");

#  使用django的filter方法过滤查询包含search的点赞通知信息   
    likedmessageall = models.Likedmessage.objects.filter(likeduser__icontains=search);

#  返回查询结果，附带查询的点赞通知信息   
    result['likedmessageall'] = objtodic(likedmessageall)
    result['message'] = "查询点赞通知成功"
    result['code'] = "202"

#  返回查询点赞通知的结果   
    return HttpResponse(json.dumps(result));


#  处理点赞通知详情   
def likedmessagedetailsjson(request):
    result = {};

#  使用request获取post中的点赞通知id参数   
    id = getQuery(request,"id");

#  根据页面传入id获取点赞通知信息   
    likedmessage = models.Likedmessage.objects.get(id=id);
    result['likedmessage'] = objtodic(likedmessage);
    result['message'] = "查询点赞通知成功"
    result['code'] = "202"

#  返回查询点赞通知详情的结果   
    return HttpResponse(json.dumps(result));


def getLikeNotificationsjson(request):
    result = {}
    
    # 获取用户ID
    userid = getQuery(request, "userid")
    
    if userid:
        # 查询该用户收到的所有点赞通知
        notifications = models.Likedmessage.objects.filter(likeduserid=userid)
        
        # 将点赞通知转换为字典格式
        result['notifications'] = objtodic(notifications)
        result['message'] = "获取点赞通知成功"
        result['code'] = "202"
    else:
        result['message'] = "未提供用户ID"
        result['code'] = "500"
    
    return HttpResponse(json.dumps(result))

def markLikeAsReadjson(request):
    result = {}
    
    # 获取点赞通知ID
    likeid = getQuery(request, "likeid")
    
    if likeid:
        try:
            # 查找并更新点赞通知的已读状态
            like = models.Likedmessage.objects.get(id=likeid)
            like.isread = '1'  # 标记为已读
            like.save()
            
            result['message'] = "标记点赞为已读成功"
            result['code'] = "202"
        except models.Likedmessage.DoesNotExist:
            result['message'] = "点赞通知不存在"
            result['code'] = "500"
    else:
        result['message'] = "未提供点赞通知ID"
        result['code'] = "500"
    
    return HttpResponse(json.dumps(result))



