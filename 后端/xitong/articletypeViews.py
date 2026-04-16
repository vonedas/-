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


#    定义添加文章分类的方法，响应页面请求
def addarticletype(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加文章分类页面，并将该页面数据传递到视图中
    return render(request, 'xitong/addarticletype.html', {});


#  处理添加文章分类方法   
def addarticletypeact(request):
    #  从页面post数据中获取分类
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  将文章分类的属性赋值给文章分类，生成文章分类对象
    articletype = models.Articletype(name=name, );

    #  调用save方法保存文章分类信息
    articletype.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加文章分类成功,并跳转到文章分类管理页面
    return HttpResponse(u"<p>添加文章分类成功</p><a href='/articletype/articletypemanage'>返回页面</a>");


#  定义表名管理方法，响应页面articletypemanage请求   
def articletypemanage(request):
    #  通过all方法查询所有的文章分类信息
    articletypeall = models.Articletype.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章分类管理页面，并附带所有文章分类信息
    return render(request, 'xitong/articletypemanage.html', {'articletypeall': articletypeall});


#  定义表名查看方法，响应页面articletypeview请求   
def articletypeview(request):
    #  通过all方法查询所有的文章分类信息
    articletypeall = models.Articletype.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章分类查看页面，并附带所有文章分类信息
    return render(request, 'xitong/articletypeview.html', {'articletypeall': articletypeall});


#  定义修改文章分类方法，通过id查询对应的文章分类信息，返回页面展示  
def updatearticletype(request, id):
    #  使用get方法，通过id查询对应的文章分类信息
    articletype = models.Articletype.objects.get(id=id);

    #  跳转到修改文章分类页面，并附带当前文章分类信息
    return render(request, 'xitong/updatearticletype.html', {'articletype': articletype, });


#  定义处理修改文章分类方法   
def updatearticletypeact(request):
    #  使用request获取post中的文章分类id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的文章分类id获取对应的文章分类信息
    articletype = models.Articletype.objects.get(id=id);

    #  从页面post数据中获取分类并赋值给articletype的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        articletype.name = namestr;

    #  调用save方法保存文章分类信息
    articletype.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改文章分类成功,并跳转到文章分类管理页面
    return HttpResponse(u"<p>修改文章分类成功</p><a href='/articletype/articletypemanage'>返回页面</a>");


#  定义删除文章分类方法   
def deletearticletypeact(request, id):
    #  调用django的delete方法，根据id删除文章分类信息
    models.Articletype.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除文章分类成功,并跳转到文章分类管理页面
    return HttpResponse(u"<p>删除文章分类成功</p><a href='/articletype/articletypemanage'>返回页面</a>");


#  定义搜索文章分类方法，响应页面搜索请求   
def searcharticletype(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的文章分类信息
    articletypeall = models.Articletype.objects.filter(name__icontains=search);

    #  跳转到搜索文章分类页面，并附带查询的文章分类信息
    return render(request, 'xitong/searcharticletype.html', {"articletypeall": articletypeall});


#  处理文章分类详情   
def articletypedetails(request, id):
    #  根据页面传入id获取文章分类信息
    articletype = models.Articletype.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到文章分类详情页面,并文章分类信息传递到页面中
    return render(request, 'xitong/articletypedetails.html', {"articletype": articletype});


#  处理添加文章分类Json方法
def addarticletypeactjson(request):
    result = {};
    # 从request中获取分类信息
    name = getQuery(request, "name");

    #  将文章分类的属性赋值给文章分类，生成文章分类对象
    articletype = models.Articletype(name=name, );

    #  调用save方法保存文章分类信息
    articletype.save();
    result['message'] = "添加文章分类成功"
    result['code'] = "202"

    #  返回添加文章分类的结果
    return HttpResponse(json.dumps(result));


#  定义处理修改文章分类方法   
def updatearticletypeactjson(request):
    result = {};

    #  使用request获取post中的文章分类id参数
    id = getQuery(request, "id");

    #  使用model的get方法根据页面传入的文章分类id获取对应的文章分类信息
    articletype = models.Articletype.objects.get(id=id);
    # 从request中获取分类信息
    name = getQuery(request, "name");
    # 如果request中存在分类信息，赋值给文章分类
    if (name != ""):
        articletype.name = name;

    #  调用save方法保存文章分类信息
    articletype.save();
    result['message'] = "修改文章分类成功"
    result['code'] = "202"

    #  返回修改文章分类的结果
    return HttpResponse(json.dumps(result));


#  定义删除文章分类方法   
def deletearticletypejson(request):
    result = {};

    #  使用request获取post中的文章分类id参数
    id = getQuery(request, "id");

    #  调用django的delete方法，根据id删除文章分类信息
    models.Articletype.objects.filter(id=id).delete();
    result['message'] = "删除文章分类成功"
    result['code'] = "202"

    #  返回删除文章分类的结果
    return HttpResponse(json.dumps(result));


#  定义搜索文章分类json方法，响应页面搜索请求   
def searcharticletypejson(request):
    result = {};

    #  获取页面post参数中的search信息
    search = getQuery(request, "search");

    #  使用django的filter方法过滤查询包含search的文章分类信息
    articletypeall = models.Articletype.objects.filter(name__icontains=search);

    #  返回查询结果，附带查询的文章分类信息
    result['articletypeall'] = objtodic(articletypeall)
    result['message'] = "查询文章分类成功"
    result['code'] = "202"

    #  返回查询文章分类的结果
    return HttpResponse(json.dumps(result));


#  处理文章分类详情   
def articletypedetailsjson(request):
    result = {};

    #  使用request获取post中的文章分类id参数
    id = getQuery(request, "id");

    #  根据页面传入id获取文章分类信息
    articletype = models.Articletype.objects.get(id=id);
    result['articletype'] = objtodic(articletype);
    result['message'] = "查询文章分类成功"
    result['code'] = "202"

    #  返回查询文章分类详情的结果
    return HttpResponse(json.dumps(result));
