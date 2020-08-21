from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry

admin.site.register(Topic) # 让 Django 通过管理网站管理我们的模型
admin.site.register(Entry)

