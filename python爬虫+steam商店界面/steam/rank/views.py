from django.shortcuts import render

# Create your views here.

# login/views.py
 
from django.shortcuts import render,redirect
 
from django.shortcuts import render,HttpResponse,redirect
from rank import models
# Create your views here.
from django.shortcuts import HttpResponse


def login(request):
    # request这是前端请求发来的请求，携带的所有数据，django给我们做了一些列的处理，封装成一个对象传过来
    # 其实挺简单，学会用它给你的一些方法就好了，其实你自己也想到它是怎样处理的。
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user_obj = models.User.objects.filter(name=name,pwd=pwd).first()
        if user_obj:
            return HttpResponse('登陆成功')
            
        else:
            return HttpResponse('用户名或密码错误')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        if name and pwd and re_pwd:
            if pwd == re_pwd:
                user_obj = models.User.objects.filter(name=name).first()
                if user_obj:
                    return HttpResponse('用户已存在')
                else:
                    models.User.objects.create(name=name,pwd=pwd).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次密码不一致')

        else:
            return HttpResponse('不能有空！')

def rank(request):
    # result=Steam.objects.all()
    return render(request,"rank.html")

def list(request):
    game_list = Steam.objects.all()
    return render(request, 'rank.html', {"game_list":game_list})