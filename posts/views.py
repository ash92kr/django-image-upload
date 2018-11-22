from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    
class PostCreate(CreateView):  # CBV
    model = Post
    fields = ['image', 'content',]  # 리스트의 마지막은 ,를 붙일 것
    # template_name = '.html' 사용하나 기본값은 _form.html 사용함
    # success_url / def get_success_url

class PostDetail(DetailView):
    model = Post
    
class PostUpdate(UpdateView):
    model = Post
    fields = ['image', 'content',]
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')  # 게시글을 삭제하므로 원래 게시글을 불러올 수 없다
    