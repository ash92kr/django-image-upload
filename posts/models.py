from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def post_image_path(instance, filename):   # Post의 instance가 instance로 들어감
    return 'posts/{}/{}'.format(instance.pk, filename)   # posts/3(pk)/유저가 업로드한 파일의 이름

# Create your models here.
class Post(models.Model):
    image = ProcessedImageField(  # imageKit에서 불러옴
            upload_to=post_image_path,  # 어디에 업로드할 것인가?
            processors=[ResizeToFill(300, 300)],   # 어떤 프로세스를 할 것인가? -> 어떻게 크기를 줄일 것인가?(Fit은 정사각형 비율로 만듦)
            format='JPEG',   # 어떤 포맷을 활용할 것인가?
            options={'quality':90},   # JPG의 압축률 사용
        )
    content = models.TextField()
    
    def get_absolute_url(self):  # self = 하나의 게시글이 생성됨
        return reverse('posts:detail', kwargs={'pk':self.pk})
    # post가 생성되거나 수정될 때 이를 만들어 어떤 상황이든 self.pk로 이동함, 주소에 번호가 들어가므로 keyword arguments가 key: value로 들어감
    # => /posts/1 -> 게시글을 생성하면 바로 그 게시글이 있는 사이트로 넘어간다
    
    

    