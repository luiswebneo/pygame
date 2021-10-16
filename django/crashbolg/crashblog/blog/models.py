from turtle import title
from venv import create
from django.db import models

#-> 3 Criando os models do blog app.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-create_at',)
    
    
    
   