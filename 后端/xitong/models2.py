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

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        dic['shijian'] = self.shijian;
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

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['name'] = self.name;
        dic['username'] = self.username;
        dic['password'] = self.password;
        dic['sex'] = self.sex;
        dic['tel'] = self.tel;
        return dic;


class Bangding(models.Model):
    id = models.AutoField(primary_key=True);
    zinv = models.CharField(max_length=500, null=True, default="");
    zinvid = models.CharField(max_length=500, null=True, default="");
    user = models.CharField(max_length=500, null=True, default="");
    userid = models.CharField(max_length=500, null=True, default="");

    def todic(self):
        dic = {};
        dic['id'] = self.id;
        dic['zinv'] = self.zinv;
        dic['zinvid'] = self.zinvid;
        dic['user'] = self.user;
        dic['userid'] = self.userid;
        return dic;
