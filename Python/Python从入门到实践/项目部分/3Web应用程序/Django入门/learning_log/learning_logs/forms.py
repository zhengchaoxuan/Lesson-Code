# 添加主题表单

from django import forms
from .models import Topic,Entry

#最简单的 ModelForm 版本只包含一个内嵌的 Meta 类，它告诉 Django 根据哪个模型创建表单，以及在表单中包含哪些字段。
class TopicForm(forms.ModelForm): 
    class Meta:
        model = Topic
        fields = {'text'} # 创建一个表单，用来包含text字段
        labels = {'text':''} # 让 Django 不要为字段 text 生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'} # 创建一个表单，用来包含text字段
        labels = {'text':''} # 让 Django 不要为字段 text 生成标签
         #小部件 （ widget ）是一个 HTML 表单元素，如单行文本框、多行文本区域, 使用 forms.Textarea ，我们定制了字段 'text' 的输入小部件
        widgets ={'text':forms.Textarea(attrs ={'cols':80} )} #默认为40        

        