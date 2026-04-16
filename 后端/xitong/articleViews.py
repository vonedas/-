# coding:utf-8
from django.db.models import QuerySet
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse, JsonResponse
from . import models
import random, os, json;
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import uuid


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


#    定义添加文章的方法，响应页面请求
def addarticle(request):
    #  获取页面数据articletype,使用DJANGO all方法查询所有数据
    articletypeall = models.Articletype.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加文章页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addarticle.html', {'articletypeall': articletypeall, });


#  处理添加文章方法   
def addarticleact(request):
    #  从页面post数据中获取标题
    titlestr = request.POST.get("title");
    title = "";
    if (titlestr is not None):
        title = titlestr;

    #  调用uploadFile方法上传页面中图片
    pic = uploadFile(request, "picfile");

    #  从页面post数据中获取内容
    contentstr = request.POST.get("content");
    content = "";
    if (contentstr is not None):
        content = contentstr;

    #  从页面post数据中获取发布时间
    addtimestr = request.POST.get("addtime");
    addtime = "";
    if (addtimestr is not None):
        addtime = addtimestr;

    #  从页面post数据中获取浏览量
    clicknumstr = request.POST.get("clicknum");
    clicknum = "";
    if (clicknumstr is not None):
        clicknum = clicknumstr;

    #  从页面post数据中获取文章分类
    articletypestr = request.POST.get("articletype");
    articletype = "";
    if (articletypestr is not None):
        articletype = articletypestr;

    #  从页面post数据中获取文章分类id
    articletypeidstr = request.POST.get("articletypeid");
    articletypeid = "";
    if (articletypeidstr is not None):
        articletypeid = articletypeidstr;

    #  将文章的属性赋值给文章，生成文章对象
    article = models.Article(title=title, pic=pic, content=content, addtime=addtime, clicknum=clicknum,
                             articletype=articletype, articletypeid=articletypeid, );

    #  调用save方法保存文章信息
    article.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加文章成功,并跳转到文章管理页面
    return HttpResponse(u"<p>添加文章成功</p><a href='/article/articlemanage'>返回页面</a>");




#  定义表名查看方法，响应页面articleview请求   
def articleview(request):
    #  通过all方法查询所有的文章信息
    articleall = models.Article.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章查看页面，并附带所有文章信息
    return render(request, 'xitong/articleview.html', {'articleall': articleall});


#  定义修改文章方法，通过id查询对应的文章信息，返回页面展示  
def updatearticle(request, id):
    #  使用get方法，通过id查询对应的文章信息
    article = models.Article.objects.get(id=id);

    #  获取页面数据articletype,使用DJANGO all方法查询所有数据
    articletypeall = models.Articletype.objects.all();

    #  跳转到修改文章页面，并附带当前文章信息
    return render(request, 'xitong/updatearticle.html', {'article': article, 'articletypeall': articletypeall, });


#  定义处理修改文章方法   
def updatearticleact(request):
    #  使用request获取post中的文章id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的文章id获取对应的文章信息
    article = models.Article.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给article的title字段
    titlestr = request.POST.get("title");
    if (titlestr is not None):
        article.title = titlestr;

    #  调用uploadFile方法上传页面中图片
    picfile = uploadFile(request, "picfile");

    #  如果picfile不等于false
    if (picfile != "false"):
        #  将picfile赋值给文章的图片字段
        article.pic = picfile;

    #  从页面post数据中获取内容并赋值给article的content字段
    contentstr = request.POST.get("content");
    if (contentstr is not None):
        article.content = contentstr;

    #  从页面post数据中获取发布时间并赋值给article的addtime字段
    addtimestr = request.POST.get("addtime");
    if (addtimestr is not None):
        article.addtime = addtimestr;

    #  从页面post数据中获取浏览量并赋值给article的clicknum字段
    clicknumstr = request.POST.get("clicknum");
    if (clicknumstr is not None):
        article.clicknum = clicknumstr;

    #  从页面post数据中获取文章分类并赋值给article的articletype字段
    articletypestr = request.POST.get("articletype");
    if (articletypestr is not None):
        article.articletype = articletypestr;

    #  从页面post数据中获取文章分类id并赋值给article的articletypeid字段
    articletypeidstr = request.POST.get("articletypeid");
    if (articletypeidstr is not None):
        article.articletypeid = articletypeidstr;

    #  调用save方法保存文章信息
    article.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改文章成功,并跳转到文章管理页面
    return HttpResponse(u"<p>修改文章成功</p><a href='/article/articlemanage'>返回页面</a>");


#  定义删除文章方法   
def deletearticleact(request, id):
    #  调用django的delete方法，根据id删除文章信息
    models.Article.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除文章成功,并跳转到文章管理页面
    return HttpResponse(u"<p>删除文章成功</p><a href='/article/articlemanage'>返回页面</a>");


def searcharticle(request):
    # 获取页面post参数中的search信息
    search = request.POST.get("search");
    articletypeid = request.POST.get("articletypeid");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";
    articletypeall = models.Articletype.objects.all();
    if articletypeid and articletypeid != 0 and articletypeid != "0":

        articleall = models.Article.objects.filter(name__icontains=search, articletypeid=articletypeid);

        return render(request, 'xitong/searcharticle.html',
                      {"articletypeall": articletypeall, "articleall": articleall, "articletypeid": int(articletypeid),
                       "search": search});
    else:
        articleall = models.Article.objects.filter(name__icontains=search);

        return render(request, 'xitong/searcharticle.html',
                      {"articletypeall": articletypeall, "articleall": articleall, "articletypeid": 0,
                       "search": search});


#  处理文章详情   
def articledetails(request, id):
    #  根据页面传入id获取文章信息
    article = models.Article.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章详情页面,并文章信息传递到页面中
    return render(request, 'xitong/articledetails.html', {"article": article});


def likedjson(request):
    result = {}

    # 获取请求参数
    articleid = getQuery(request, 'articleid')
    userid = getQuery(request, 'userid')
    user = getQuery(request, 'user')
    type = getQuery(request, 'type')

    if type == '0':  # 查询是否点赞
        likednum = models.Liked.objects.filter(articleid=articleid, userid=userid).count()
        result['likednum'] = likednum
        result['code'] = "202"

    elif type == '1':  # 添加点赞
        # 检查是否已经点赞
        if models.Liked.objects.filter(articleid=articleid, userid=userid).count() == 0:
            article = models.Article.objects.get(id=articleid)
            liked = models.Liked(
                articleid=articleid,
                userid=userid,
                user=user,
                article=article.title
            )
            liked.save()
            result['message'] = "点赞成功"
            result['code'] = "202"
        else:
            result['message'] = "已经点赞过了"
            result['code'] = "500"

    elif type == '2':  # 取消点赞
        models.Liked.objects.filter(articleid=articleid, userid=userid).delete()
        result['message'] = "取消点赞成功"
        result['code'] = "202"

    elif type == '3':  # 获取点赞数量
        likednum = models.Liked.objects.filter(articleid=articleid).count()
        result['likednum'] = likednum
        result['code'] = "202"

    return HttpResponse(json.dumps(result))


def collectedjson(request):
    result = {}

    # 获取请求参数
    articleid = getQuery(request, 'articleid')
    userid = getQuery(request, 'userid')
    user = getQuery(request, 'user')
    type = getQuery(request, 'type')

    if type == '0':  # 查询是否收藏
        collectednum = models.Collected.objects.filter(articleid=articleid, userid=userid).count()
        result['collectednum'] = collectednum
        result['code'] = "202"

    elif type == '1':  # 添加收藏
        # 检查是否已经收藏
        if models.Collected.objects.filter(articleid=articleid, userid=userid).count() == 0:
            article = models.Article.objects.get(id=articleid)
            collected = models.Collected(
                articleid=articleid,
                userid=userid,
                user=user,
                article=article.title
            )
            collected.save()
            result['message'] = "收藏成功"
            result['code'] = "202"
        else:
            result['message'] = "已经收藏过了"
            result['code'] = "500"

    elif type == '2':  # 取消收藏
        models.Collected.objects.filter(articleid=articleid, userid=userid).delete()
        result['message'] = "取消收藏成功"
        result['code'] = "202"

    elif type == '3':  # 获取收藏数量
        collectednum = models.Collected.objects.filter(articleid=articleid).count()
        result['collectednum'] = collectednum
        result['code'] = "202"

    return HttpResponse(json.dumps(result))


#  处理添加文章Json方法
def addarticleactjson(request):
    result = {};
    # 从request中获取标题信息
    title = getQuery(request, "title");
    # 从request中获取图片信息
    pic = getQuery(request, "pic");
    # 从request中获取内容信息
    content = getQuery(request, "content");
    # 从request中获取发布时间信息
    addtime = getQuery(request, "addtime");
    # 从request中获取浏览量信息
    clicknum = getQuery(request, "clicknum");
    # 从request中获取文章分类信息
    articletype = getQuery(request, "articletype");
    # 从request中获取文章分类id信息
    articletypeid = getQuery(request, "articletypeid");

    #  将文章的属性赋值给文章，生成文章对象
    article = models.Article(title=title, pic=pic, content=content, addtime=addtime, clicknum=clicknum,
                             articletype=articletype, articletypeid=articletypeid, );

    #  调用save方法保存文章信息
    article.save();
    result['message'] = "添加文章成功"
    result['code'] = "202"

    #  返回添加文章的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改文章方法   
def updatearticleactjson(request):
    result = {};

    #  使用request获取post中的文章id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的文章id获取对应的文章信息
    article = models.Article.objects.get(id=id);
    # 从request中获取标题信息
    title = getQuery(request, "title");
    # 如果request中存在标题信息，赋值给文章
    if (title != ""):
        article.title = title;
    # 从request中获取图片信息
    pic = getQuery(request, "pic");
    # 如果request中存在图片信息，赋值给文章
    if (pic != ""):
        article.pic = pic;
    # 从request中获取内容信息
    content = getQuery(request, "content");
    # 如果request中存在内容信息，赋值给文章
    if (content != ""):
        article.content = content;
    # 从request中获取发布时间信息
    addtime = getQuery(request, "addtime");
    # 如果request中存在发布时间信息，赋值给文章
    if (addtime != ""):
        article.addtime = addtime;
    # 从request中获取浏览量信息
    clicknum = getQuery(request, "clicknum");
    # 如果request中存在浏览量信息，赋值给文章
    if (clicknum != ""):
        article.clicknum = clicknum;
    # 从request中获取文章分类信息
    articletype = getQuery(request, "articletype");
    # 如果request中存在文章分类信息，赋值给文章
    if (articletype != ""):
        article.articletype = articletype;
    # 从request中获取文章分类id信息
    articletypeid = getQuery(request, "articletypeid");
    # 如果request中存在文章分类id信息，赋值给文章
    if (articletypeid != ""):
        article.articletypeid = articletypeid;

    #  调用save方法保存文章信息
    article.save();
    result['message'] = "修改文章成功"
    result['code'] = "202"

    #  返回修改文章的结果
    return HttpResponse(json.dumps(result));


#  定义删除文章方法   
def deletearticlejson(request):
    result = {};

    #  使用request获取post中的文章id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除文章信息
    models.Article.objects.filter(id=id).delete();
    result['message'] = "删除文章成功"
    result['code'] = "202"

    #  返回删除文章的结果
    return HttpResponse(json.dumps(result));


#  定义搜索文章json方法，响应页面搜索请求   
def searcharticlejson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的文章信息
    articleall = models.Article.objects.filter(title__icontains=search);

    #  返回查询结果，附带查询的文章信息
    result['articleall'] = objtodic(articleall)
    result['message'] = "查询文章成功"
    result['code'] = "202"

    #  返回查询文章的结果
    return HttpResponse(json.dumps(result));


#  处理文章详情   
def articledetailsjson(request):
    result = {};

    #  使用request获取post中的文章id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取文章信息
    article = models.Article.objects.get(id=id);
    result['article'] = objtodic(article);
    result['message'] = "查询文章成功"
    result['code'] = "202"

    #  返回查询文章详情的结果
    return HttpResponse(json.dumps(result));


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # 生成唯一的文件名
            ext = os.path.splitext(image.name)[1]
            filename = f"{uuid.uuid4().hex}{ext}"

            # 确保上传目录存在
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'article_images')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # 保存文件
            filepath = os.path.join(upload_dir, filename)
            with open(filepath, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # 返回文件URL
            file_url = f"/media/article_images/{filename}"
            return JsonResponse({
                "errno": 0,
                "data": {
                    "url": file_url,
                    "alt": filename,
                    "href": file_url
                }
            })

    return JsonResponse({
        "errno": 1,
        "message": "上传失败"
    })


def searcharticlebytypejson(request):
    result = {}

    # 获取搜索关键词和分类ID
    search = getQuery(request, "search")
    articletypeid = getQuery(request, "articletypeid")

    # 如果search为None，设置为空字符串
    if search is None:
        search = ""

    # 构建查询条件
    if articletypeid and articletypeid != "0":
        # 按分类和标题搜索
        articleall = models.Article.objects.filter(
            title__icontains=search,
            articletypeid=articletypeid
        )
    else:
        # 只按标题搜索
        articleall = models.Article.objects.filter(
            title__icontains=search
        )

    # 返回查询结果
    result['articleall'] = objtodic(articleall)
    result['message'] = "查询文章成功"
    result['code'] = "202"

    return HttpResponse(json.dumps(result))


def updateclicknumjson(request):
    result = {}

    # 获取文章ID
    id = getQuery(request, "id")

    try:
        # 获取文章对象
        article = models.Article.objects.get(id=id)

        # 增加浏览量
        article.clicknum = article.clicknum + 1
        article.save()

        result['message'] = "更新浏览量成功"
        result['code'] = "202"
    except:
        result['message'] = "更新浏览量失败"
        result['code'] = "500"

    return HttpResponse(json.dumps(result))


# 推荐文章
def recoArticle(request, id):
    # 统计当前推荐数量
    reco_count = models.Article.objects.filter(isreco='是').count()
    if reco_count >= 8:
        return HttpResponse("<script>alert('最多只能推荐8篇文章');window.location.href='/article/articlemanage';</script>")
    article = models.Article.objects.get(id=id)
    article.isreco = '是'
    article.save()
    return HttpResponse("<script>alert('推荐成功');window.location.href='/article/articlemanage';</script>")

# 取消推荐
def unrecoArticle(request, id):
    article = models.Article.objects.get(id=id)
    article.isreco = '否'
    article.save()
    return HttpResponse("<script>alert('已取消推荐');window.location.href='/article/articlemanage';</script>")

# 修改articlemanage推荐排序
def articlemanage(request):
    # 推荐的文章在前，且最多8个
    reco_articles = list(models.Article.objects.filter(isreco='是')[:8])
    other_articles = list(models.Article.objects.exclude(id__in=[a.id for a in reco_articles]))
    articleall = reco_articles + other_articles
    backurl = request.POST.get("backurl")
    if (backurl is not None):
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>")
    return render(request, 'xitong/articlemanage.html', {'articleall': articleall})

# 获取推荐文章
def getRecommendedArticles(request):
    result = {}
    try:
        # 获取所有被推荐的文章
        articles = models.Article.objects.filter(isreco='是').order_by('-addtime')
        result['articles'] = objtodic(articles)
        result['message'] = "获取推荐文章成功"
        result['code'] = "202"
    except Exception as e:
        result['message'] = f"获取推荐文章失败: {str(e)}"
        result['code'] = "500"
    return HttpResponse(json.dumps(result))