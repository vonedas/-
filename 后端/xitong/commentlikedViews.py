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


#    定义添加评论点赞的方法，响应页面请求
def addcommentliked(request):
    #  获取页面数据articlecomment,使用DJANGO all方法查询所有数据
    articlecommentall = models.Articlecomment.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加评论点赞页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addcommentliked.html',
                  {'articlecommentall': articlecommentall, 'userall': userall, });


#  处理添加评论点赞方法   
def addcommentlikedact(request):
    #  从页面post数据中获取文章评论id
    articlecommentidstr = request.POST.get("articlecommentid");
    articlecommentid = "";
    if (articlecommentidstr is not None):
        articlecommentid = articlecommentidstr;

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

    #  将评论点赞的属性赋值给评论点赞，生成评论点赞对象
    commentliked = models.Commentliked(articlecommentid=articlecommentid, user=user, userid=userid, );

    #  调用save方法保存评论点赞信息
    commentliked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加评论点赞成功,并跳转到评论点赞管理页面
    return HttpResponse(u"<p>添加评论点赞成功</p><a href='/commentliked/commentlikedmanage'>返回页面</a>");


#  定义表名管理方法，响应页面commentlikedmanage请求   
def commentlikedmanage(request):
    #  通过all方法查询所有的评论点赞信息
    commentlikedall = models.Commentliked.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到评论点赞管理页面，并附带所有评论点赞信息
    return render(request, 'xitong/commentlikedmanage.html', {'commentlikedall': commentlikedall});


#  定义表名查看方法，响应页面commentlikedview请求   
def commentlikedview(request):
    #  通过all方法查询所有的评论点赞信息
    commentlikedall = models.Commentliked.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到评论点赞查看页面，并附带所有评论点赞信息
    return render(request, 'xitong/commentlikedview.html', {'commentlikedall': commentlikedall});


#  定义修改评论点赞方法，通过id查询对应的评论点赞信息，返回页面展示  
def updatecommentliked(request, id):
    #  使用get方法，通过id查询对应的评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);

    #  获取页面数据articlecomment,使用DJANGO all方法查询所有数据
    articlecommentall = models.Articlecomment.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改评论点赞页面，并附带当前评论点赞信息
    return render(request, 'xitong/updatecommentliked.html',
                  {'commentliked': commentliked, 'articlecommentall': articlecommentall, 'userall': userall, });


#  定义处理修改评论点赞方法   
def updatecommentlikedact(request):
    #  使用request获取post中的评论点赞id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的评论点赞id获取对应的评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);

    #  从页面post数据中获取文章评论id并赋值给commentliked的articlecommentid字段
    articlecommentidstr = request.POST.get("articlecommentid");
    if (articlecommentidstr is not None):
        commentliked.articlecommentid = articlecommentidstr;

    #  从页面post数据中获取用户并赋值给commentliked的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        commentliked.user = userstr;

    #  从页面post数据中获取用户id并赋值给commentliked的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        commentliked.userid = useridstr;

    #  调用save方法保存评论点赞信息
    commentliked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改评论点赞成功,并跳转到评论点赞管理页面
    return HttpResponse(u"<p>修改评论点赞成功</p><a href='/commentliked/commentlikedmanage'>返回页面</a>");


#  定义删除评论点赞方法   
def deletecommentlikedact(request, id):
    #  调用django的delete方法，根据id删除评论点赞信息
    models.Commentliked.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除评论点赞成功,并跳转到评论点赞管理页面
    return HttpResponse(u"<p>删除评论点赞成功</p><a href='/commentliked/commentlikedmanage'>返回页面</a>");


#  定义搜索评论点赞方法，响应页面搜索请求   
def searchcommentliked(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的评论点赞信息
    commentlikedall = models.Commentliked.objects.filter(articlecommentid__icontains=search);

    #  跳转到搜索评论点赞页面，并附带查询的评论点赞信息
    return render(request, 'xitong/searchcommentliked.html', {"commentlikedall": commentlikedall});


#  处理评论点赞详情   
def commentlikeddetails(request, id):
    #  根据页面传入id获取评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到评论点赞详情页面,并评论点赞信息传递到页面中
    return render(request, 'xitong/commentlikeddetails.html', {"commentliked": commentliked});


#  定义跳转user添加评论点赞页面的方法  
def useraddcommentliked(request):
    #  获取页面数据articlecomment,使用DJANGO all方法查询所有数据
    articlecommentall = models.Articlecomment.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加评论点赞页面
    return render(request, 'xitong/useraddcommentliked.html',
                  {'articlecommentall': articlecommentall, 'userall': userall, });


#  处理添加评论点赞方法   
def useraddcommentlikedact(request):
    #  从页面post数据中获取文章评论id
    articlecommentidstr = request.POST.get("articlecommentid");
    articlecommentid = "";
    if (articlecommentidstr is not None):
        articlecommentid = articlecommentidstr;

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

    #  将评论点赞的属性赋值给评论点赞，生成评论点赞对象
    commentliked = models.Commentliked(articlecommentid=articlecommentid, user=user, userid=userid, );

    #  调用save方法保存评论点赞信息
    commentliked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加评论点赞成功,并跳转到评论点赞管理页面
    return HttpResponse(u"<p>添加评论点赞成功</p><a href='/commentliked/usercommentlikedmanage'>返回页面</a>");


#  跳转user评论点赞管理页面
def usercommentlikedmanage(request):
    #  查询出userid等于当前用户id的所有评论点赞信息
    commentlikedall = models.Commentliked.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回评论点赞管理页面，并携带commentlikedall的数据信息
    return render(request, 'xitong/usercommentlikedmanage.html', {'commentlikedall': commentlikedall});


#  定义跳转user修改评论点赞页面      
def userupdatecommentliked(request, id):
    #  根据页面传入的评论点赞id信息，查询出对应的评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);

    #  获取页面数据articlecomment,使用DJANGO all方法查询所有数据
    articlecommentall = models.Articlecomment.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改评论点赞页面，并携带查询出的评论点赞信息
    return render(request, 'xitong/userupdatecommentliked.html',
                  {'commentliked': commentliked, 'articlecommentall': articlecommentall, 'userall': userall, });


#  定义处理修改评论点赞方法   
def userupdatecommentlikedact(request):
    #  使用request获取post中的评论点赞id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的评论点赞id获取对应的评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);

    #  从页面post数据中获取文章评论id并赋值给commentliked的articlecommentid字段
    articlecommentidstr = request.POST.get("articlecommentid");
    if (articlecommentidstr is not None):
        commentliked.articlecommentid = articlecommentidstr;

    #  从页面post数据中获取用户并赋值给commentliked的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        commentliked.user = userstr;

    #  从页面post数据中获取用户id并赋值给commentliked的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        commentliked.userid = useridstr;

    #  调用save方法保存评论点赞信息
    commentliked.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改评论点赞成功,并跳转到评论点赞管理页面
    return HttpResponse(u"<p>修改评论点赞成功</p><a href='/commentliked/usercommentlikedmanage'>返回页面</a>");


#  定义user删除评论点赞信息
def userdeletecommentlikedact(request, id):
    #  根据页面传入的评论点赞id信息，删除出对应的评论点赞信息
    models.Commentliked.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除评论点赞成功，并跳转到评论点赞管理页面
    return HttpResponse(u"<p>删除评论点赞成功</p><a href='/commentliked/usercommentlikedmanage'>返回页面</a>");


#  处理添加评论点赞Json方法
def addcommentlikedactjson(request):
    result = {};
    # 从request中获取文章评论id信息
    articlecommentid = getQuery(request, "articlecommentid");
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");

    #  将评论点赞的属性赋值给评论点赞，生成评论点赞对象
    commentliked = models.Commentliked(articlecommentid=articlecommentid, user=user, userid=userid, );

    #  调用save方法保存评论点赞信息
    commentliked.save();
    result['message'] = "添加评论点赞成功"
    result['code'] = "202"

    #  返回添加评论点赞的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改评论点赞方法   
def updatecommentlikedactjson(request):
    result = {};

    #  使用request获取post中的评论点赞id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的评论点赞id获取对应的评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);
    # 从request中获取文章评论id信息
    articlecommentid = getQuery(request, "articlecommentid");
    # 如果request中存在文章评论id信息，赋值给评论点赞
    if (articlecommentid != ""):
        commentliked.articlecommentid = articlecommentid;
    # 从request中获取用户信息
    user = getQuery(request, "user");
    # 如果request中存在用户信息，赋值给评论点赞
    if (user != ""):
        commentliked.user = user;
    # 从request中获取用户id信息
    userid = getQuery(request, "userid");
    # 如果request中存在用户id信息，赋值给评论点赞
    if (userid != ""):
        commentliked.userid = userid;

    #  调用save方法保存评论点赞信息
    commentliked.save();
    result['message'] = "修改评论点赞成功"
    result['code'] = "202"

    #  返回修改评论点赞的结果
    return HttpResponse(json.dumps(result));


#  定义删除评论点赞方法   
def deletecommentlikedjson(request):
    result = {};

    #  使用request获取post中的评论点赞id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除评论点赞信息
    models.Commentliked.objects.filter(id=id).delete();
    result['message'] = "删除评论点赞成功"
    result['code'] = "202"

    #  返回删除评论点赞的结果
    return HttpResponse(json.dumps(result));


#  定义搜索评论点赞json方法，响应页面搜索请求   
def searchcommentlikedjson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的评论点赞信息
    commentlikedall = models.Commentliked.objects.filter(articlecommentid__icontains=search);

    #  返回查询结果，附带查询的评论点赞信息
    result['commentlikedall'] = objtodic(commentlikedall)
    result['message'] = "查询评论点赞成功"
    result['code'] = "202"

    #  返回查询评论点赞的结果
    return HttpResponse(json.dumps(result));


#  处理评论点赞详情   
def commentlikeddetailsjson(request):
    result = {};

    #  使用request获取post中的评论点赞id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取评论点赞信息
    commentliked = models.Commentliked.objects.get(id=id);
    result['commentliked'] = objtodic(commentliked);
    result['message'] = "查询评论点赞成功"
    result['code'] = "202"

    #  返回查询评论点赞详情的结果
    return HttpResponse(json.dumps(result));


def commentlikedjson(request):
    result = {}
    
    # 获取评论ID和用户ID
    articlecommentid = getQuery(request, "articlecommentid")
    userid = getQuery(request, "userid")
    
    # 查询是否已点赞
    likednum = models.Commentliked.objects.filter(articlecommentid=articlecommentid, userid=userid).count()
    
    result['likednum'] = likednum
    result['code'] = "202"
    
    return HttpResponse(json.dumps(result))

def addcommentlikedjson(request):
    result = {}
    
    # 获取评论ID和用户信息
    articlecommentid = getQuery(request, "articlecommentid")
    user = getQuery(request, "user")
    userid = getQuery(request, "userid")
    
    # 检查是否已经点赞
    if models.Commentliked.objects.filter(articlecommentid=articlecommentid, userid=userid).count() == 0:
        # 添加点赞记录
        commentliked = models.Commentliked(
            articlecommentid=articlecommentid,
            user=user,
            userid=userid
        )
        commentliked.save()
        
        # 更新评论的点赞数
        comment = models.Articlecomment.objects.get(id=articlecommentid)
        if comment.likenum is None:
            comment.likenum = 1
        else:
            comment.likenum = comment.likenum + 1
        comment.save()
        
        result['message'] = "点赞成功"
        result['code'] = "202"
    else:
        result['message'] = "已经点赞过了"
        result['code'] = "500"
    
    return HttpResponse(json.dumps(result))

def cancelcommentlikedjson(request):
    result = {}
    
    # 获取评论ID和用户ID
    articlecommentid = getQuery(request, "articlecommentid")
    userid = getQuery(request, "userid")
    
    # 删除点赞记录
    models.Commentliked.objects.filter(articlecommentid=articlecommentid, userid=userid).delete()
    
    # 更新评论的点赞数
    comment = models.Articlecomment.objects.get(id=articlecommentid)
    if comment.likenum is not None and comment.likenum > 0:
        comment.likenum = comment.likenum - 1
        comment.save()
    
    result['message'] = "取消点赞成功"
    result['code'] = "202"
    
    return HttpResponse(json.dumps(result))
