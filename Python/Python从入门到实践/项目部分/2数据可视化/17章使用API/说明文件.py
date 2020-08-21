'''
这章学习的是Web应用编程接口API，其可视化信息来自于Github -- 无聊可以去查找一些公开的API
1.1.调用Github的API-----了解-https://api.github.com/search/repositories?q=language:python&sort=stars 的意思
1.2.安装requests库 -唯一的一个非转基因的 Python HTTP 库
1.3. 处理api响应
1.4. 生成api响应的字典，并且对于字典进行简单处理得到有效信息输出（描述github关于python的最受欢迎的库）
1.5 监视API的速率限制 -- 在浏览器输入    https://api.github.com/rate_limit   进行查看并且简单了解
1.6 使用pygal进行可视化设置

date:2020/08/10
2.1 改进pygal图表，增加了Config函数进行图表的配置 ------处理api响应.py
2.2 添加自定义工具提示 ---- 字典：'value':数据进行绘制直线图，'label':描述数据的描述 -----添加自定义描述.py
2.3 添加可单击的链接   ---- 在字典中添加'xlink' ------处理api响应.py

--1.问题：“AttributeError: 'NoneType' object has no attribute 'decode'” ---- 里面还有对象是空的，即有个参数为none，无属性
解决:使用对此参数加上是否为none的if--else判断

2.4 进行练习获得简单网易新闻 --- from operator import itemsgetter  ->可以在字典使用sorted函数时，key = itemsgetter('comment'),其可以传递键comment,使用键的值进行排列
2.5 进行测试代码
'''