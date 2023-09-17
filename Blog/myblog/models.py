from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(max_length=300)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Article:{self.title} author: {self.author}"
    def __repr__(self) -> str:
        return f"Article:{self.title} author: {self.author}"
    
        
