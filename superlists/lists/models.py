from django.db import models

# Create your models here.
class Item(models.Model):
    # 没有长度限制的字符串类型字段
    text = models.TextField(default="")