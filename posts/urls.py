from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [      # function으로 바꾸기
    path('', views.PostList.as_view(), name='list'),
]