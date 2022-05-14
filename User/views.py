import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from User.models import UserInfo, UserBase
from User.utils.encryption import Encryption
from User.utils.utils import Utils


# Create your views here.

def login(request):
    # 如果请求
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    date = Utils().login(userName=username, pwd=password)
    print(date)
    if date == '登陆成功':
        response = HttpResponseRedirect('/user/info/')
        # 下发cookie,有效期360秒
        user_MMID = username + '_' + str(int(time.time()))
        USER_MMID = Encryption.des_encrypt(user_MMID)
        # 往库中插入cookie
        UserBase.objects.filter(username=username).update(USER_MMID=USER_MMID)
        response.set_cookie('USER_MMID', USER_MMID, 360)
        return response
    return HttpResponseRedirect(reverse("login"), {"date": '帐号密码错误'})


def register(request):
    if request.method == "GET":
        question = Utils().get_question()
        user_list = Utils().get_username()

        return render(request, "register.html", {"question": question, "user_list": user_list})

    # 获取用户填写的数据

    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    username = request.POST.get("username")
    Email = request.POST.get("Email")
    password = request.POST.get("password")
    repeatpassword = request.POST.get("repeatpassword")
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    # permission = request.POST.get("permission")

    print(request.POST)

    # 将获取的数据写入到数据库中

    date = Utils().register(username=username, password=password, lastname=lastname,
                            firstname=firstname, Email=Email, question=question,
                            answer=answer, repeatpassword=repeatpassword)
    print(date)
    if date == '注册成功':
        return HttpResponseRedirect(reverse("login"), {"date": '注册成功'})
    response = HttpResponseRedirect('/user/register/')
    return response


def Test(request):
    date = UserBase.objects.get(username="hehaodong123")
    print(date.username)
    return HttpResponse(date)


def info(request):
    # 读取客户端请求携带的cookie，如果不为空，表示为已登录帐号
    USER_MMID = request.COOKIES.get('USER_MMID', '')
    print(USER_MMID)
    if not USER_MMID:
        return HttpResponseRedirect('/user/login/')
    return render(request, 'info.html')
