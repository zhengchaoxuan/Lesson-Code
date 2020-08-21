from django.shortcuts import render
from django.http import HttpResponseRedirect # 用户提交主题后我们将使用这个类将用户重定向到网页 topics 
from django.urls import reverse  #根据指定的 URL 模型确定 URL ，这意味着 Django将在页面被请求时生成 URL
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """注销账户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''注册账户'''
    if request.method !='POST':
        form = UserCreationForm() #不提供任何实例，如果要实例，使用instance，并且要导入实例
    else:
        form = UserCreationForm(data = request.POST) #根据提交的数据进行创建表单
        #判断是否数据错误
        if form.is_valid():
            new_user = form.save() #保存到数据库，并且生成对象继续用户自动登录
            #让用户自动登录，再重定向回主页,方法 authenticate() 将返回一个通过了身份验证的用户对象，而我们将其存储在 authenticated_user 中
            #自动登录
            authenticated_user = authenticate(username = new_user.username,password = request.POST['password1'])
            login(request,authenticated_user)
            #重定向回主页
            return HttpResponseRedirect(reverse('learning_logs:index')) 
    context = {'form':form}
    return render(request,'users/register.html',context)


