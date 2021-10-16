from django.contrib import admin

#-> 4 Registrando os modelos aqui.

from .models import Post

admin.site.register(Post)
