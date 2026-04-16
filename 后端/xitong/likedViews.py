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


#    定义添加点赞的方法，响应页面请求
def addliked(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加点赞页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addliked.html', {'userall': userall, 'articleall': articleall, });


#  处理添加点赞方法   
def addlikedact(request):
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

    #  从页面post数据中获取文章
    articlestr = request.POST.get("article");
    article = "";
    if (articlestr is not None):
        article = articlestr;

    #  从页面post数据中获取文章id
    articleidstr = request.POST.get("articleid");
    articleid = "";
    if (articleidstr is not None):
        articleid = articleidstr;

    #  将点赞的属性赋值给点赞，生成点赞对象
    liked = models.Liked(user=user, userid=userid, article=article, articleid=articleid, );

    #  调用save方法保存点赞信息
    liked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加点赞成功,并跳转到点赞管理页面
    return HttpResponse(u"<p>添加点赞成功</p><a href='/liked/likedmanage'>返回页面</a>");


#  定义表名管理方法，响应页面likedmanage请求   
def likedmanage(request):
    #  通过all方法查询所有的点赞信息
    likedall = models.Liked.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到点赞管理页面，并附带所有点赞信息
    return render(request, 'xitong/likedmanage.html', {'likedall': likedall});


#  定义表名查看方法，响应页面likedview请求   
def likedview(request):
    #  通过all方法查询所有的点赞信息
    likedall = models.Liked.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到点赞查看页面，并附带所有点赞信息
    return render(request, 'xitong/likedview.html', {'likedall': likedall});


#  定义修改点赞方法，通过id查询对应的点赞信息，返回页面展示  
def updateliked(request, id):
    #  使用get方法，通过id查询对应的点赞信息
    liked = models.Liked.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  跳转到修改点赞页面，并附带当前点赞信息
    return render(request, 'xitong/updateliked.html', {'liked': liked, 'userall': userall, 'articleall': articleall, });


#  定义处理修改点赞方法   
def updatelikedact(request):
    #  使用request获取post中的点赞id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的点赞id获取对应的点赞信息
    liked = models.Liked.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给liked的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        liked.user = userstr;

    #  从页面post数据中获取用户id并赋值给liked的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        liked.userid = useridstr;

    #  从页面post数据中获取文章并赋值给liked的article字段
    articlestr = request.POST.get("article");
    if (articlestr is not None):
        liked.article = articlestr;

    #  从页面post数据中获取文章id并赋值给liked的articleid字段
    articleidstr = request.POST.get("articleid");
    if (articleidstr is not None):
        liked.articleid = articleidstr;

    #  调用save方法保存点赞信息
    liked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改点赞成功,并跳转到点赞管理页面
    return HttpResponse(u"<p>修改点赞成功</p><a href='/liked/likedmanage'>返回页面</a>");


#  定义删除点赞方法   
def deletelikedact(request, id):
    #  调用django的delete方法，根据id删除点赞信息
    models.Liked.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除点赞成功,并跳转到点赞管理页面
    return HttpResponse(u"<p>删除点赞成功</p><a href='/liked/likedmanage'>返回页面</a>");


#  定义搜索点赞方法，响应页面搜索请求   
def searchliked(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的点赞信息
    likedall = models.Liked.objects.filter(user__icontains=search);

    #  跳转到搜索点赞页面，并附带查询的点赞信息
    return render(request, 'xitong/searchliked.html', {"likedall": likedall});


#  处理点赞详情   
def likeddetails(request, id):
    #  根据页面传入id获取点赞信息
    liked = models.Liked.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到点赞详情页面,并点赞信息传递到页面中
    return render(request, 'xitong/likeddetails.html', {"liked": liked});


#  定义跳转user添加点赞页面的方法  
def useraddliked(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加点赞页面
    return render(request, 'xitong/useraddliked.html', {'userall': userall, 'articleall': articleall, });


#  处理添加点赞方法   
def useraddlikedact(request):
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

    #  从页面post数据中获取文章
    articlestr = request.POST.get("article");
    article = "";
    if (articlestr is not None):
        article = articlestr;

    #  从页面post数据中获取文章id
    articleidstr = request.POST.get("articleid");
    articleid = "";
    if (articleidstr is not None):
        articleid = articleidstr;

    #  将点赞的属性赋值给点赞，生成点赞对象
    liked = models.Liked(user=user, userid=userid, article=article, articleid=articleid, );

    #  调用save方法保存点赞信息
    liked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加点赞成功,并跳转到点赞管理页面
    return HttpResponse(u"<p>添加点赞成功</p><a href='/liked/userlikedmanage'>返回页面</a>");


#  跳转user点赞管理页面
def userlikedmanage(request):
    #  查询出userid等于当前用户id的所有点赞信息
    likedall = models.Liked.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回点赞管理页面，并携带likedall的数据信息
    return render(request, 'xitong/userlikedmanage.html', {'likedall': likedall});


#  定义跳转user修改点赞页面      
def userupdateliked(request, id):
    #  根据页面传入的点赞id信息，查询出对应的点赞信息
    liked = models.Liked.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  跳转到修改点赞页面，并携带查询出的点赞信息
    return render(request, 'xitong/userupdateliked.html',
                  {'liked': liked, 'userall': userall, 'articleall': articleall, });


#  定义处理修改点赞方法   
def userupdatelikedact(request):
    #  使用request获取post中的点赞id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的点赞id获取对应的点赞信息
    liked = models.Liked.objects.get(id=id);

    #  从页面post数据中获取用户并赋值给liked的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        liked.user = userstr;

    #  从页面post数据中获取用户id并赋值给liked的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        liked.userid = useridstr;

    #  从页面post数据中获取文章并赋值给liked的article字段
    articlestr = request.POST.get("article");
    if (articlestr is not None):
        liked.article = articlestr;

    #  从页面post数据中获取文章id并赋值给liked的articleid字段
    articleidstr = request.POST.get("articleid");
    if (articleidstr is not None):
        liked.articleid = articleidstr;

    #  调用save方法保存点赞信息
    liked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改点赞成功,并跳转到点赞管理页面
    return HttpResponse(u"<p>修改点赞成功</p><a href='/liked/userlikedmanage'>返回页面</a>");


#  定义user删除点赞信息
def userdeletelikedact(request, id):
    #  根据页面传入的点赞id信息，删除出对应的点赞信息
    models.Liked.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除点赞成功，并跳转到点赞管理页面
    return HttpResponse(u"<p>删除点赞成功</p><a href='/liked/userlikedmanage'>返回页面</a>");


#  处理添加点赞Json方法
def addlikedactjson(request):
    result = {};
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取文章信息
    article = getQuery(request, "article");
    # 从request中获取文章id信息
    articleid = getQuery(request, "articleid");

    #  将点赞的属性赋值给点赞，生成点赞对象
    liked = models.Liked(user=user, userid=userid, article=article, articleid=articleid, );

    #  调用save方法保存点赞信息
    liked.save();
    result['message'] = "添加点赞成功"
    result['code'] = "202"

    #  返回添加点赞的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改点赞方法   
def updatelikedactjson(request):
    result = {};

    #  使用request获取post中的点赞id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的点赞id获取对应的点赞信息
    liked = models.Liked.objects.get(id=id);
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给点赞
    if (user != ""):
        liked.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给点赞
    if (userid != ""):
        liked.userid = userid;
    # 从request中获取文章信息
    article = getQuery(request, "article");
    # 如果request中存在文章信息，赋值给点赞
    if (article != ""):
        liked.article = article;
    # 从request中获取文章id信息
    articleid = getQuery(request, "articleid");
    # 如果request中存在文章id信息，赋值给点赞
    if (articleid != ""):
        liked.articleid = articleid;

    #  调用save方法保存点赞信息
    liked.save();
    result['message'] = "修改点赞成功"
    result['code'] = "202"

    #  返回修改点赞的结果
    return HttpResponse(json.dumps(result));


#  定义删除点赞方法   
def deletelikedjson(request):
    result = {};

    #  使用request获取post中的点赞id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除点赞信息
    models.Liked.objects.filter(id=id).delete();
    result['message'] = "删除点赞成功"
    result['code'] = "202"

    #  返回删除点赞的结果
    return HttpResponse(json.dumps(result));


#  定义搜索点赞json方法，响应页面搜索请求   
def searchlikedjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的点赞信息
    likedall = models.Liked.objects.filter(user__icontains=search);

    #  返回查询结果，附带查询的点赞信息
    result['likedall'] = objtodic(likedall)
    result['message'] = "查询点赞成功"
    result['code'] = "202"

    #  返回查询点赞的结果
    return HttpResponse(json.dumps(result));


#  处理点赞详情   
def likeddetailsjson(request):
    result = {};

    #  使用request获取post中的点赞id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取点赞信息
    liked = models.Liked.objects.get(id=id);
    result['liked'] = objtodic(liked);
    result['message'] = "查询点赞成功"
    result['code'] = "202"

    #  返回查询点赞详情的结果
    return HttpResponse(json.dumps(result));
