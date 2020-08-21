from django.db import models

# Create your models here.
class Topping(models.Model):
    '''用户学习的主题'''
     # 属性默认为类属性（可以给直接被类本身调用）
    name = models.CharField(max_length=200) # CharField -- 由字符或文本组成的数据,可储存存储少量的文本，如名称、标题或城市
    date_added = models.DateTimeField(auto_now_add=True) # DateTimeField —— 记录日期和时间的数据, 将这个属性自动设置成当前日期和时间

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.name
