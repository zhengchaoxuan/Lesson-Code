'''
使用Django框架来进行一个名为‘Learning Log’的项目

date:2020/08/11
18-1 建立项目
1. 安装virtualenv
2. 建立虚拟环境
3. 激活虚拟环境 -- 可以在环境中安装包，并使用安装包(只在活动状态可以用) --ll_env\Scripts\activate
4. 安装Django  pip install Django
5. 在Django中创建项目 -- django-admin.py startproject learning_log .  并且了解各个py文件的功能
6. 创建数据库 -- python manage.py migrate  我们将修改数据库称为 迁移 数据库。首次执行命令 migrate 时，将让 Django 确保数据库与项目的当前状态匹配。
   ----在使用 SQLite （后面将更详细地介绍）的新项目中首次执行这个命令时， Django 将新建一个数据库。 Django 指出它将创建必要的数据库表，
   ----用于存储我们将在这个项目（ Synchronize unmigrated apps ， 同步未迁移的应用程序 ）中使用的信息，再确保数据库结构与当前代码（ Apply all migrations ， 应用所有的迁移 ）匹配。
7. 查看项目 -- python manage.py runserver 
8. 创建应用程序 --- python manage.py startapp learning_logs--让 Django 建立创建应用程序所需的基础设施（runserver运行着）

date:2020/08/12
1.定义模型 -- models.py 进行定义 Chirdfiled和datetimefirld并使用__str__返回
2.激活模型 -- setting.py 将应用程序包含到项目,Powershell 调用 makemigrations ；让 Django 迁移项目

date：2020/08/13
18-2 Django 管理网站
1. 创建超级用户 --powershell:python manage.py createsuperuser ---  Django 并不存储你输入的密码，而存储从该密码派生出来的一个字符串 —— 散列值

2. 向管理网站注册模型--admin.py  -Django 自动在管理网站中添加了一些模型，如 User 和 Group ，但对于我们创建的模型，必须手工进行注册

3. 定义Entry模型 -- modern.py 
-> migrations 迁移模型 Entry由于我们添加了一个新模型，因此需要再次迁移数据库
->向管理网站注册 Entry  admin.py 更改，如何使用runserver进行查看

4.使用shell ---这种交互式环境称为 Django shell ，是测试项目和排除其故障的理想之地

18-3 创建网页：学习笔记主页
1. 映射URL  --- 这部分要注意到path替代url(版本问题),已经有一个admin的URL了，添加另一个网站主页作为学习主页 
-->在app应用程序的文件夹添加另一个urls.py文件，添加view模块

2.编写视图和模板 --- views.py添加 index模块  在添加index.html #必须在templates/app_name/

18-4 创建其他的网页
1. 模板继承 -- 模板标签 子模板和父模板 {% block content %}{% endblock content %}
2. 显示所有的主题页面  --- 在项目中添加URL，如何进行View.py->编写HTML
3. 显示特定主题的页面 ---re_path
'''
