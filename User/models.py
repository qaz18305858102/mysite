from django.db import models


# Create your models here.


# 1、创建，修改，删除数据库表
# 2、执行命令 python manage.py makemigrations User
# 3、执行命令 python manage.py migrate


class UserBase(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    permission = models.CharField(max_length=30, default="员工")
    USER_MMID = models.CharField(max_length=100, default="")
    creat_time = models.DateTimeField(auto_now_add=True)
    updtae_time = models.DateTimeField(auto_now=True)


class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    Email = models.CharField(max_length=30)
    question = models.CharField(max_length=30)
    answer = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    updtae_time = models.DateTimeField(auto_now=True)


class Question(models.Model):
    question = models.CharField(max_length=30)
