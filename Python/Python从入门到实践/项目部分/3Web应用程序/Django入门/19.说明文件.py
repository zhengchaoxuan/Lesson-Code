'''
学习目标：
1. 创建一些表单，让用户能够添加主题和条目，以及编辑既有的条目
2. 学习 Django 如何防范对基于表单的网页发起的常见攻击
3. 实现用户身份验证系统
4. 学习如何确保用户数据的安全
'''
'''
19.1 　让用户能够输入数据
内容:
1. 添加新主题  -> urls.py添加
2. 用于添加主题的表单 ->在models.py 目录添加forms.py 加入djgango的forms 和自己的Topic,使用ModelForm 版本只包含一个内嵌的 Meta 类导入Topic数据生成表格
3. 生成视图 -> views.py 考虑GET 请求和 POST 请求并且把把form放入数据库
4. 生成模板 -> new_topic.html文件 生成HTML表格并且进行预防攻击表格
5. 添加新的条目 -> 在表格forms.py进行定义
6. 编辑条目

19.2 创建用户账户
学习目标：
1. 创建一个新的应用程序，其中包含与处理用户账户相关的所有功能
2. 对模型 Topic 稍做修改，让每个主题都归属于特定用户

内容:
1. 进行设置user登录界面
2. 进行注销
'''
