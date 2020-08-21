from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
     # 属性默认为类属性（可以给直接被类本身调用）
    owner = models.ForeignKey(User,on_delete=models.CASCADE) # 关联用户，然后使用shell查看，然后进行数据更新
    text = models.CharField(max_length=200) # CharField -- 由字符或文本组成的数据,可储存存储少量的文本，如名称、标题或城市
    date_added = models.DateTimeField(auto_now_add=True) # DateTimeField —— 记录日期和时间的数据, 将这个属性自动设置成当前日期和时间

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.text

class Entry(models.Model):
    """ 学到的有关某个主题的具体知识 """
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ 返回模型的字符串表示 """
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return self.text





