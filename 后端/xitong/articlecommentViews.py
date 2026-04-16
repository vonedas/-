# coding:utf-8
from django.db.models import QuerySet, Q
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


#    定义添加文章评论的方法，响应页面请求
def addarticlecomment(request):
    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加文章评论页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addarticlecomment.html', {'articleall': articleall, 'userall': userall, });


#  处理添加文章评论方法   
def addarticlecommentact(request):
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

    #  从页面post数据中获取用户头像
    userpicstr = request.POST.get("userpic");
    userpic = "";
    if (userpicstr is not None):
        userpic = userpicstr;

    #  从页面post数据中获取根评论id
    rootidstr = request.POST.get("rootid");
    rootid = "";
    if (rootidstr is not None):
        rootid = rootidstr;

    #  从页面post数据中获取父评论id
    parentidstr = request.POST.get("parentid");
    parentid = "";
    if (parentidstr is not None):
        parentid = parentidstr;

    #  从页面post数据中获取评论层级
    levelstr = request.POST.get("level");
    level = "";
    if (levelstr is not None):
        level = levelstr;

    #  从页面post数据中获取评论时间
    commenttimestr = request.POST.get("commenttime");
    commenttime = "";
    if (commenttimestr is not None):
        commenttime = commenttimestr;

    #  从页面post数据中获取是否已读
    isreadstr = request.POST.get("isread");
    isread = "";
    if (isreadstr is not None):
        isread = isreadstr;

    #  将文章评论的属性赋值给文章评论，生成文章评论对象
    articlecomment = models.Articlecomment(article=article, articleid=articleid, user=user, userid=userid,
                                           userpic=userpic, rootid=rootid, parentid=parentid, level=level,
                                           commenttime=commenttime, isread=isread, );

    #  调用save方法保存文章评论信息
    articlecomment.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加文章评论成功,并跳转到文章评论管理页面
    return HttpResponse(u"<p>添加文章评论成功</p><a href='/articlecomment/articlecommentmanage'>返回页面</a>");


#  定义表名管理方法，响应页面articlecommentmanage请求   
def articlecommentmanage(request):
    #  通过all方法查询所有的文章评论信息
    articlecommentall = models.Articlecomment.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章评论管理页面，并附带所有文章评论信息
    return render(request, 'xitong/articlecommentmanage.html', {'articlecommentall': articlecommentall});


#  定义表名查看方法，响应页面articlecommentview请求   
def articlecommentview(request):
    #  通过all方法查询所有的文章评论信息
    articlecommentall = models.Articlecomment.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章评论查看页面，并附带所有文章评论信息
    return render(request, 'xitong/articlecommentview.html', {'articlecommentall': articlecommentall});


#  定义修改文章评论方法，通过id查询对应的文章评论信息，返回页面展示  
def updatearticlecomment(request, id):
    #  使用get方法，通过id查询对应的文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);

    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改文章评论页面，并附带当前文章评论信息
    return render(request, 'xitong/updatearticlecomment.html',
                  {'articlecomment': articlecomment, 'articleall': articleall, 'userall': userall, });


#  定义处理修改文章评论方法   
def updatearticlecommentact(request):
    #  使用request获取post中的文章评论id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的文章评论id获取对应的文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);

    #  从页面post数据中获取文章并赋值给articlecomment的article字段
    articlestr = request.POST.get("article");
    if (articlestr is not None):
        articlecomment.article = articlestr;

    #  从页面post数据中获取文章id并赋值给articlecomment的articleid字段
    articleidstr = request.POST.get("articleid");
    if (articleidstr is not None):
        articlecomment.articleid = articleidstr;

    #  从页面post数据中获取用户并赋值给articlecomment的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        articlecomment.user = userstr;

    #  从页面post数据中获取用户id并赋值给articlecomment的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        articlecomment.userid = useridstr;

    #  从页面post数据中获取用户头像并赋值给articlecomment的userpic字段
    userpicstr = request.POST.get("userpic");
    if (userpicstr is not None):
        articlecomment.userpic = userpicstr;

    #  从页面post数据中获取根评论id并赋值给articlecomment的rootid字段
    rootidstr = request.POST.get("rootid");
    if (rootidstr is not None):
        articlecomment.rootid = rootidstr;

    #  从页面post数据中获取父评论id并赋值给articlecomment的parentid字段
    parentidstr = request.POST.get("parentid");
    if (parentidstr is not None):
        articlecomment.parentid = parentidstr;

    #  从页面post数据中获取评论层级并赋值给articlecomment的level字段
    levelstr = request.POST.get("level");
    if (levelstr is not None):
        articlecomment.level = levelstr;

    #  从页面post数据中获取评论时间并赋值给articlecomment的commenttime字段
    commenttimestr = request.POST.get("commenttime");
    if (commenttimestr is not None):
        articlecomment.commenttime = commenttimestr;

    #  从页面post数据中获取是否已读并赋值给articlecomment的isread字段
    isreadstr = request.POST.get("isread");
    if (isreadstr is not None):
        articlecomment.isread = isreadstr;

    #  调用save方法保存文章评论信息
    articlecomment.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改文章评论成功,并跳转到文章评论管理页面
    return HttpResponse(u"<p>修改文章评论成功</p><a href='/articlecomment/articlecommentmanage'>返回页面</a>");


#  定义删除文章评论方法   
def deletearticlecommentact(request, id):
    #  调用django的delete方法，根据id删除文章评论信息
    models.Articlecomment.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除文章评论成功,并跳转到文章评论管理页面
    return HttpResponse(u"<p>删除文章评论成功</p><a href='/articlecomment/articlecommentmanage'>返回页面</a>");


#  定义搜索文章评论方法，响应页面搜索请求   
def searcharticlecomment(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的文章评论信息
    articlecommentall = models.Articlecomment.objects.filter(article__icontains=search);

    #  跳转到搜索文章评论页面，并附带查询的文章评论信息
    return render(request, 'xitong/searcharticlecomment.html', {"articlecommentall": articlecommentall});


#  处理文章评论详情   
def articlecommentdetails(request, id):
    #  根据页面传入id获取文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章评论详情页面,并文章评论信息传递到页面中
    return render(request, 'xitong/articlecommentdetails.html', {"articlecomment": articlecomment});


#  定义跳转user添加文章评论页面的方法  
def useraddarticlecomment(request):
    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加文章评论页面
    return render(request, 'xitong/useraddarticlecomment.html', {'articleall': articleall, 'userall': userall, });


#  处理添加文章评论方法   
def useraddarticlecommentact(request):
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

    #  从页面post数据中获取用户头像
    userpicstr = request.POST.get("userpic");
    userpic = "";
    if (userpicstr is not None):
        userpic = userpicstr;

    #  从页面post数据中获取根评论id
    rootidstr = request.POST.get("rootid");
    rootid = "";
    if (rootidstr is not None):
        rootid = rootidstr;

    #  从页面post数据中获取父评论id
    parentidstr = request.POST.get("parentid");
    parentid = "";
    if (parentidstr is not None):
        parentid = parentidstr;

    #  从页面post数据中获取评论层级
    levelstr = request.POST.get("level");
    level = "";
    if (levelstr is not None):
        level = levelstr;

    #  从页面post数据中获取评论时间
    commenttimestr = request.POST.get("commenttime");
    commenttime = "";
    if (commenttimestr is not None):
        commenttime = commenttimestr;

    #  从页面post数据中获取是否已读
    isreadstr = request.POST.get("isread");
    isread = "";
    if (isreadstr is not None):
        isread = isreadstr;

    #  将文章评论的属性赋值给文章评论，生成文章评论对象
    articlecomment = models.Articlecomment(article=article, articleid=articleid, user=user, userid=userid,
                                           userpic=userpic, rootid=rootid, parentid=parentid, level=level,
                                           commenttime=commenttime, isread=isread, );

    #  调用save方法保存文章评论信息
    articlecomment.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加文章评论成功,并跳转到文章评论管理页面
    return HttpResponse(u"<p>添加文章评论成功</p><a href='/articlecomment/userarticlecommentmanage'>返回页面</a>");


#  跳转user文章评论管理页面
def userarticlecommentmanage(request):
    #  查询出userid等于当前用户id的所有文章评论信息
    articlecommentall = models.Articlecomment.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回文章评论管理页面，并携带articlecommentall的数据信息
    return render(request, 'xitong/userarticlecommentmanage.html', {'articlecommentall': articlecommentall});


#  定义跳转user修改文章评论页面      
def userupdatearticlecomment(request, id):
    #  根据页面传入的文章评论id信息，查询出对应的文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);

    #  获取页面数据article,使用DJANGO all方法查询所有数据
    articleall = models.Article.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改文章评论页面，并携带查询出的文章评论信息
    return render(request, 'xitong/userupdatearticlecomment.html',
                  {'articlecomment': articlecomment, 'articleall': articleall, 'userall': userall, });


#  定义处理修改文章评论方法   
def userupdatearticlecommentact(request):
    #  使用request获取post中的文章评论id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的文章评论id获取对应的文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);

    #  从页面post数据中获取文章并赋值给articlecomment的article字段
    articlestr = request.POST.get("article");
    if (articlestr is not None):
        articlecomment.article = articlestr;

    #  从页面post数据中获取文章id并赋值给articlecomment的articleid字段
    articleidstr = request.POST.get("articleid");
    if (articleidstr is not None):
        articlecomment.articleid = articleidstr;

    #  从页面post数据中获取用户并赋值给articlecomment的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        articlecomment.user = userstr;

    #  从页面post数据中获取用户id并赋值给articlecomment的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        articlecomment.userid = useridstr;

    #  从页面post数据中获取用户头像并赋值给articlecomment的userpic字段
    userpicstr = request.POST.get("userpic");
    if (userpicstr is not None):
        articlecomment.userpic = userpicstr;

    #  从页面post数据中获取根评论id并赋值给articlecomment的rootid字段
    rootidstr = request.POST.get("rootid");
    if (rootidstr is not None):
        articlecomment.rootid = rootidstr;

    #  从页面post数据中获取父评论id并赋值给articlecomment的parentid字段
    parentidstr = request.POST.get("parentid");
    if (parentidstr is not None):
        articlecomment.parentid = parentidstr;

    #  从页面post数据中获取评论层级并赋值给articlecomment的level字段
    levelstr = request.POST.get("level");
    if (levelstr is not None):
        articlecomment.level = levelstr;

    #  从页面post数据中获取评论时间并赋值给articlecomment的commenttime字段
    commenttimestr = request.POST.get("commenttime");
    if (commenttimestr is not None):
        articlecomment.commenttime = commenttimestr;

    #  从页面post数据中获取是否已读并赋值给articlecomment的isread字段
    isreadstr = request.POST.get("isread");
    if (isreadstr is not None):
        articlecomment.isread = isreadstr;

    #  调用save方法保存文章评论信息
    articlecomment.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改文章评论成功,并跳转到文章评论管理页面
    return HttpResponse(u"<p>修改文章评论成功</p><a href='/articlecomment/userarticlecommentmanage'>返回页面</a>");


#  定义user删除文章评论信息
def userdeletearticlecommentact(request, id):
    #  根据页面传入的文章评论id信息，删除出对应的文章评论信息
    models.Articlecomment.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除文章评论成功，并跳转到文章评论管理页面
    return HttpResponse(u"<p>删除文章评论成功</p><a href='/articlecomment/userarticlecommentmanage'>返回页面</a>");


#  处理添加文章评论Json方法
def addarticlecommentactjson(request):
    result = {};
    # 从request中获取文章信息
    article = getQuery(request, "article");
    # 从request中获取文章id信息
    articleid = getQuery(request, "articleid");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 从request中获取用户头像信息
    userpic = getQuery(request, "userpic");
    # 从request中获取根评论id信息
    rootid = getQuery(request, "rootid");
    # 从request中获取父评论id信息
    parentid = getQuery(request, "parentid");
    # 从request中获取评论层级信息
    level = getQuery(request, "level");
    # 从request中获取评论时间信息
    commenttime = getQuery(request, "commenttime");
    # 从request中获取是否已读信息
    isread = getQuery(request, "isread");

    content = getQuery(request, "content");

    likenum = getQuery(request, "likenum");

    #  将文章评论的属性赋值给文章评论，生成文章评论对象
    articlecomment = models.Articlecomment(article=article, articleid=articleid, user=user, userid=userid,
                                           userpic=userpic, rootid=rootid, parentid=parentid, level=level,
                                           commenttime=commenttime, isread=isread, content=content, likenum=likenum,);

    #  调用save方法保存文章评论信息
    articlecomment.save();
    result['message'] = "添加文章评论成功"
    result['code'] = "202"

    #  返回添加文章评论的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改文章评论方法   
def updatearticlecommentactjson(request):
    result = {};

    #  使用request获取post中的文章评论id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的文章评论id获取对应的文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);
    # 从request中获取文章信息
    article = getQuery(request, "article");
    # 如果request中存在文章信息，赋值给文章评论
    if (article != ""):
        articlecomment.article = article;
    # 从request中获取文章id信息
    articleid = getQuery(request, "articleid");
    # 如果request中存在文章id信息，赋值给文章评论
    if (articleid != ""):
        articlecomment.articleid = articleid;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给文章评论
    if (user != ""):
        articlecomment.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给文章评论
    if (userid != ""):
        articlecomment.userid = userid;
    # 从request中获取用户头像信息
    userpic = getQuery(request, "userpic");
    # 如果request中存在用户头像信息，赋值给文章评论
    if (userpic != ""):
        articlecomment.userpic = userpic;
    # 从request中获取根评论id信息
    rootid = getQuery(request, "rootid");
    # 如果request中存在根评论id信息，赋值给文章评论
    if (rootid != ""):
        articlecomment.rootid = rootid;
    # 从request中获取父评论id信息
    parentid = getQuery(request, "parentid");
    # 如果request中存在父评论id信息，赋值给文章评论
    if (parentid != ""):
        articlecomment.parentid = parentid;
    # 从request中获取评论层级信息
    level = getQuery(request, "level");
    # 如果request中存在评论层级信息，赋值给文章评论
    if (level != ""):
        articlecomment.level = level;
    # 从request中获取评论时间信息
    commenttime = getQuery(request, "commenttime");
    # 如果request中存在评论时间信息，赋值给文章评论
    if (commenttime != ""):
        articlecomment.commenttime = commenttime;
    # 从request中获取是否已读信息
    isread = getQuery(request, "isread");
    # 如果request中存在是否已读信息，赋值给文章评论
    if (isread != ""):
        articlecomment.isread = isread;

    #  调用save方法保存文章评论信息
    articlecomment.save();
    result['message'] = "修改文章评论成功"
    result['code'] = "202"

    #  返回修改文章评论的结果
    return HttpResponse(json.dumps(result));


#  定义删除文章评论方法   
def deletearticlecommentjson(request):
    result = {};

    #  使用request获取post中的文章评论id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除文章评论信息
    models.Articlecomment.objects.filter(id=id).delete();
    result['message'] = "删除文章评论成功"
    result['code'] = "202"

    #  返回删除文章评论的结果
    return HttpResponse(json.dumps(result));


#  定义搜索文章评论json方法，响应页面搜索请求   
def searcharticlecommentjson(request):
    result = {}

    # 获取文章ID
    articleid = getQuery(request, "articleid")

    # 查询指定文章的所有评论，按评论时间排序
    articlecommentall = models.Articlecomment.objects.filter(articleid=articleid).order_by('commenttime')

    # 返回查询结果
    result['articlecommentall'] = objtodic(articlecommentall)
    result['message'] = "查询评论成功"
    result['code'] = "202"

    return HttpResponse(json.dumps(result))


#  处理文章评论详情   
def articlecommentdetailsjson(request):
    result = {};

    #  使用request获取post中的文章评论id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取文章评论信息
    articlecomment = models.Articlecomment.objects.get(id=id);
    result['articlecomment'] = objtodic(articlecomment);
    result['message'] = "查询文章评论成功"
    result['code'] = "202"

    #  返回查询文章评论详情的结果
    return HttpResponse(json.dumps(result));


def getCommentNotificationsjson(request):
    result = {}
    
    # 获取用户ID
    userid = getQuery(request, "userid")
    
    if userid:
        try:
            # 获取所有评论
            allComments = models.Articlecomment.objects.all()
            
            # 第一次遍历：找出用户发布的所有评论ID
            userCommentIds = []
            for comment in allComments:
                if comment.userid == int(userid):
                    userCommentIds.append(comment.id)
            
            # 第二次遍历：找出回复了用户评论的所有评论
            replyComments = []
            for comment in allComments:
                # 检查该评论的rootid或parentid是否在用户的评论ID列表中
                if (comment.rootid in userCommentIds or comment.parentid in userCommentIds):
                    replyComments.append(comment.todic())  # 直接转换为字典
            
            # 直接使用转换好的字典列表
            result['notifications'] = replyComments
            result['message'] = "获取评论通知成功"
            result['code'] = "202"
        except Exception as e:
            result['message'] = str(e)
            result['code'] = "500"
    else:
        result['message'] = "未提供用户ID"
        result['code'] = "500"
    
    return HttpResponse(json.dumps(result))

def markCommentAsReadjson(request):
    result = {}
    
    # 获取评论ID
    commentid = getQuery(request, "commentid")
    
    if commentid:
        try:
            # 查找并更新评论的已读状态
            comment = models.Articlecomment.objects.get(id=commentid)
            comment.isread = '1'  # 标记为已读
            comment.save()
            
            result['message'] = "标记评论为已读成功"
            result['code'] = "202"
        except models.Articlecomment.DoesNotExist:
            result['message'] = "评论不存在"
            result['code'] = "500"
    else:
        result['message'] = "未提供评论ID"
        result['code'] = "500"
    
    return HttpResponse(json.dumps(result))
