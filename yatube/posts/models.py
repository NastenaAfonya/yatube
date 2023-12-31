from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts" )
    group = models.ForeignKey(Group)
    
class Group(models.Model):
    title = models.TextField() # Имя группы
    slug = models.TextField() # уникальный адрес группы, часть URL (например, для группы любителей котиков slug будет равен cats: group/cats)
    description = models.TextField() # текст, который появляется на странице сообщества
    
