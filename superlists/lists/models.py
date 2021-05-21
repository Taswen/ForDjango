from django.db import models

class List(models.Model):
    pass

# Create your models here.
class Item(models.Model):
    # 没有长度限制的字符串类型字段
    text = models.TextField(default="")
    list = models.ForeignKey(List,on_delete=models.CASCADE, default=None)
