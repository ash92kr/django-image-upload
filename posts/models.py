from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    content = models.TextField()
    
    def get_absolute_url(self):  # self = 하나의 게시글이 생성됨
        return reverse('posts:detail', kwargs={'pk':self.pk})
    # post가 생성되거나 수정될 때 이를 만들어 어떤 상황이든 self.pk로 이동함, 주소에 번호가 들어가므로 keyword arguments가 key: value로 들어감
    # => /posts/1 -> 게시글을 생성하면 바로 그 게시글이 있는 사이트로 넘어간다