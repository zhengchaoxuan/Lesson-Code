from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404 # 用户提交主题后我们将使用这个类将用户重定向到网页 topics 
from django.urls import reverse  #根据指定的 URL 模型确定 URL ，这意味着 Django将在页面被请求时生成 URL

from .models import Topic,Entry
from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')  #属性 date_added 对它们进行排序
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    '''显示特定的主题'''
    topic = Topic.objects.get(id = topic_id)

    if topic.owner !=request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added') #date_added 前面的减号指定按降序排列，即先显示最近的条目
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method!='POST':
        #未提交数据:创建一个列表
        form = TopicForm()
    else:
        #提交数据，并对数据进行处理
        form  = TopicForm(request.POST)
        if form.is_valid(): #是否有效
            new_topic = form.save(commit =False) # 把表单数据保存到数据库
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics')) # reverse() 获取页面 topics 的 URL ，并将其传递给 HttpResponseRedirect() 
    
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    #从数据库先取出具体的model对象
    topic = Topic.objects.get(id = topic_id) # 输入id
    if request.method !='POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid:
            # 此处的save有commit=False参数，意思是只生成model对象，而不保存，生成的model对象new_article就可以修改了
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            # 列表 args ，其中包含要包含在 URL 中的所有实参
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id])) 

    context ={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """进行编辑条目"""
    entry = Entry.objects.get(id = entry_id) #获得条目信息
    topic = entry.topic # 获得条目关联的主题

    if topic.owner !=request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry,data = request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topic",args = [topic.id]))
    
    context = {'topic':topic,'entry':entry,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)



             


    


