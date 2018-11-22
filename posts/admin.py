from django.contrib import admin
from .models import Post   # 현재 폴더의 models에서 Post 클래스를 가져올 것

# Register your models here.
admin.site.register(Post)

