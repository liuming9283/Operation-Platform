# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import models
# Create your views here.

# 参数都要默认加一个"request", request封装了用户请求的所有内容
# request.POST 用户以POST方式提交的所有数据
# request.GET 用户以GET方式提交的所有数据
def home(request):
    return HttpResponse("OK")

def page(request,n1,n2):
    nic = n1 + n2
    return HttpResponse(nic)

def index(request):
    return render(request, 'index.html')

#简单的数据库操作
def db_handle(request):
    # 增
    # dic = {"username":"li","password":"123","age":13}
    # models.Userinfo.objects.create(**dic)

    # 删
    # models.Userinfo.objects.filter(id=1).delete()

    # 改
    # models.Userinfo.objects.filter(age=13).update(age=18)

    # 查
    # models.Host.objects.filter(system_type='linux' hostname__contains='cent')  查询主机名中包含cent的项，返回一个列表
    # models.Host.objects.filter(id__gt=2)  查询id大于2的项
    # models.Host.objects.filter(id__in=[1,2,3,4,5]) 查询id为1,2,3,4,5的项，没有就不返回
    # models.Host.objects.get(system_type='linux', hostname__contains='centos')  为精确查找，返回一个具体的项 ，只能返回一个值
    # info = models.Userinfo.objects.all().first()
    # return HttpResponse(info.username+u" 年龄:"+str(info.age))

    # def __unicode__(self):
    #   如果用get或其他方法返回，可能会得到<XXXXX: XXXXX object>  这是需要这个方法
    #     # 在Python3中使用 def __str__(self)
    #     return self.info

    if request.method == "POST":
        models.Userinfo.objects.create(username=request.POST["username"],
                                       password=request.POST["password"],
                                       age=int(request.POST["age"]))


    user_info = models.Userinfo.objects.all() # user_info 为Userinfo的类对象列表  叫做“queryset”类型
    return render(request, "t1.html", {"name": u"用户表", "li": user_info})

"""
对以下四个部分加装饰器，可以让用户必须以login为网站的入口，否则无法浏览内容
login_required通过判断session来阻止用户访问其他页面4
"""
@login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def host(request):
    return render(request, 'host.html')

@login_required
def audit(request):
    return render(request, 'audit.html')

@login_required
def asset(request):
    return render(request, 'asset.html')

def acc_login(request):
    # print request.POST
    # request.POST的内容如下：
    # <QueryDict: {u'username': [u'weber'], u'csrfmiddlewaretoken': [u'XC8Jf8PBFIclESMa4VgIYwl39qgYX19v'], u'password': [u'123456']}>

    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        # user = authenticate(**{"username":uname,"password":pwd})  #两种传参方式
        user = authenticate(username=uname, password=pwd)
        if user is not None:  # 验证通过
            login(request, user)   #通过此方法产生session
            return HttpResponseRedirect("/homepage/")
        else:
            return render(request, 'login.html', {'login_err':"登录失败，用户名或密码错误！！！"})
    else:
        return render(request, 'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def register(request):
    if request.method == "POST":
        print request.POST
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        email = request.POST.get("email")

        if len(User.objects.filter(username=uname)) == 0:    # 判断用户表中是否重名
            user = User.objects.create_user(uname, email, pwd)
            user.save()
            return render(request, 'register.html', {"success":"success!!! You can try login"})
        else:
            return render(request, 'register.html', {"repeat": "failed!! The username has been registed"})
    else:
        return render(request, 'register.html')


def testurl(request):
    return render(request, 'login2.html')