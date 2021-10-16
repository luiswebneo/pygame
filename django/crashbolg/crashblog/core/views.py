from django.http import request
from django.shortcuts import render

from blog.models import Post

#-> 1 fazendo a requisições para o core/base.html
def frontpage(request):
    posts = Post.objects.all()
    
    return render(request, 'core/frontpage.html', {'posts': posts})

#-> 2 fazendo a requisição para o core/about.html
def about(request):
    return render(request, 'core/about.html')
