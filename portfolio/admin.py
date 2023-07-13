from django.contrib import admin
from .models import Project
from blog.models import Post

admin.site.register(Project)
admin.site.register(Post)