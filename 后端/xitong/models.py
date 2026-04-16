from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True);
    username = models.CharField(max_length=500, null=True, default="");
    password = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['username'] = self.username;
        dic['password'] = self.password;
        return dic;


class User(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    username = models.CharField(max_length=500, null=True, default="");
    password = models.CharField(max_length=500, null=True, default="");
    pic = models.CharField(max_length=500, null=True, default="");
    gender = models.CharField(max_length=500, null=True, default="");
    age = models.CharField(max_length=500, null=True, default="");
    shengao = models.CharField(max_length=500, null=True, default="");
    tizhong = models.CharField(max_length=500, null=True, default="");
    tel = models.CharField(max_length=500, null=True, default="");
    duanlian = models.CharField(max_length=500, null=True, default="");
    xuqiu = models.CharField(max_length=500, null=True, default="");
    status = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['username'] = self.username;
        dic['password'] = self.password;
        dic['pic'] = self.pic;
        dic['gender'] = self.gender;
        dic['age'] = self.age;
        dic['shengao'] = self.shengao;
        dic['tizhong'] = self.tizhong;
        dic['tel'] = self.tel;
        dic['duanlian'] = self.duanlian;
        dic['xuqiu'] = self.xuqiu;
        dic['status'] = self.status;
        return dic;


class Tizhong(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    shijian = models.CharField(max_length=500, null=True, default="");
    shuju = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['shijian'] = self.shijian;
        dic['shuju'] = self.shuju;
        return dic;


class Yao(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    shijian = models.CharField(max_length=500, null=True, default="");
    daka = models.CharField(max_length=500, null=True, default="");
    date = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['shijian'] = self.shijian;
        dic['daka'] = self.daka;
        return dic;


class Yinshilog(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    kaluli = models.CharField(max_length=500, null=True, default="");
    shijian = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['kaluli'] = self.kaluli;
        dic['shijian'] = self.shijian;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        return dic;


class Notice(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    pic = models.CharField(max_length=500, null=True, default="");
    neirong = models.CharField(max_length=500, null=True, default="");
    shijian = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['pic'] = self.pic;
        dic['neirong'] = self.neirong;
        dic['shijian'] = self.shijian;
        return dic;


class Xueya(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    shuzhi = models.CharField(max_length=500, null=True, default="");
    leixing = models.CharField(max_length=500, null=True, default="");
    shijian = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['shuzhi'] = self.shuzhi;
        dic['leixing'] = self.leixing;
        dic['shijian'] = self.shijian;
        return dic;


class Duanlianlog(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    kaluli = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    shijian = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['kaluli'] = self.kaluli;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['shijian'] = self.shijian;
        return dic;


class Zinv(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    username = models.CharField(max_length=500, null=True, default="");
    password = models.CharField(max_length=500, null=True, default="");
    sex = models.CharField(max_length=500, null=True, default="");
    tel = models.CharField(max_length=500, null=True, default="");
    pic = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['username'] = self.username;
        dic['password'] = self.password;
        dic['sex'] = self.sex;
        dic['tel'] = self.tel;
        dic['pic'] = self.pic;
        return dic;


class Bangding(models.Model):
    id = models.AutoField(primary_key=True);
    zinv = models.CharField(max_length=500, null=True, default="");
    zinvid = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    status = models.IntegerField(default=0);

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['zinv'] = self.zinv;
        dic['zinvid'] = self.zinvid;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        return dic;


class Motiontype(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");
    danwei = models.CharField(max_length=500, null=True, default="");
    value = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['danwei'] = self.danwei;
        dic['value'] = self.value;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        return dic;


class Healthrecord(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    name = models.CharField(max_length=500, null=True, default="");
    shangxian = models.CharField(max_length=500, null=True, default="");
    xiaxian = models.CharField(max_length=500, null=True, default="");
    danwei = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['name'] = self.name;
        dic['shangxian'] = self.shangxian;
        dic['xiaxian'] = self.xiaxian;
        dic['danwei'] = self.danwei;
        return dic;


class Recordhealth(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    healthrecord = models.CharField(max_length=500, null=True, default="");
    healthrecordid = models.CharField(max_length=500, null=True, default="");
    shangxian = models.CharField(max_length=500, null=True, default="");
    xiaxian = models.CharField(max_length=500, null=True, default="");
    danwei = models.CharField(max_length=500, null=True, default="");
    value = models.CharField(max_length=500, null=True, default="");
    recordtime = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['healthrecord'] = self.healthrecord;
        dic['healthrecordid'] = self.healthrecordid;
        dic['shangxian'] = self.shangxian;
        dic['xiaxian'] = self.xiaxian;
        dic['danwei'] = self.danwei;
        dic['value'] = self.value;
        dic['recordtime'] = self.recordtime;
        return dic;


class Article(models.Model):
    id = models.AutoField(primary_key=True);
    title = models.CharField(max_length=500, null=True, default="");
    pic = models.CharField(max_length=500, null=True, default="");
    content = models.CharField(max_length=500, null=True, default="");
    addtime = models.CharField(max_length=500, null=True, default="");
    clicknum = models.CharField(max_length=500, null=True, default="");
    articletype = models.CharField(max_length=500, null=True, default="");
    articletypeid = models.CharField(max_length=500, null=True, default="");
    isreco = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['title'] = self.title;
        dic['pic'] = self.pic;
        dic['content'] = self.content;
        dic['addtime'] = self.addtime;
        dic['clicknum'] = self.clicknum;
        dic['articletype'] = self.articletype;
        dic['articletypeid'] = self.articletypeid;
        dic['isreco'] = self.isreco;
        return dic;


class Articletype(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        return dic;


class Liked(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    article = models.CharField(max_length=500, null=True, default="");
    articleid = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['article'] = self.article;
        dic['articleid'] = self.articleid;
        return dic;


class Collected(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    article = models.CharField(max_length=500, null=True, default="");
    articleid = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['article'] = self.article;
        dic['articleid'] = self.articleid;
        return dic;


class Articlecomment(models.Model):
    id = models.AutoField(primary_key=True);
    article = models.CharField(max_length=500, null=True, default="");
    articleid = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");
    userpic = models.CharField(max_length=500, null=True, default="");
    rootid = models.CharField(max_length=500, null=True, default="");
    parentid = models.CharField(max_length=500, null=True, default="");
    level = models.CharField(max_length=500, null=True, default="");
    commenttime = models.CharField(max_length=500, null=True, default="");
    isread = models.CharField(max_length=500, null=True, default="");
    content = models.CharField(max_length=500, null=True, default="");
    likenum = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['article'] = self.article;
        dic['articleid'] = self.articleid;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['userpic'] = self.userpic;
        dic['rootid'] = self.rootid;
        dic['parentid'] = self.parentid;
        dic['level'] = self.level;
        dic['commenttime'] = self.commenttime;
        dic['isread'] = self.isread;
        dic['content'] = self.content;
        dic['likenum'] = self.likenum;
        return dic;



class Commentliked(models.Model):
    id = models.AutoField(primary_key=True);
    articlecommentid = models.CharField(max_length=500,null=True,default="");
    user = models.CharField(max_length=500,null=True,default="");
    userid = models.CharField(max_length=500,null=True,default="");
    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['articlecommentid'] = self.articlecommentid;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        return dic;



class Likedmessage(models.Model):
    id = models.AutoField(primary_key=True);
    likeduser = models.CharField(max_length=500,null=True,default="");
    likeduserid = models.CharField(max_length=500,null=True,default="");
    user = models.CharField(max_length=500,null=True,default="");
    userid = models.CharField(max_length=500,null=True,default="");
    isread = models.CharField(max_length=500,null=True,default="");
    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['likeduser'] = self.likeduser;
        dic['likeduserid'] = self.likeduserid;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['isread'] = self.isread;
        return dic;

class Auth(models.Model):
    id = models.AutoField(primary_key=True);
    userid = models.CharField(max_length=500,null=True,default="");
    authid = models.CharField(max_length=500,null=True,default="");
    bloodpressure = models.BooleanField(default=True)
    tizhong = models.BooleanField(default=True)
    xuqiu = models.BooleanField(default=True)
    duanlian = models.BooleanField(default=True)
    diet = models.BooleanField(default=True)
    exercise = models.BooleanField(default=True)
    medicine = models.BooleanField(default=True)

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['userid'] = self.userid;
        dic['authid'] = self.authid;
        dic['bloodpressure'] = self.bloodpressure;
        dic['tizhong'] = self.tizhong;
        dic['xuqiu'] = self.xuqiu;
        dic['diet'] = self.diet;
        dic['exercise'] = self.exercise;
        dic['medicine'] = self.medicine;
        return dic;
