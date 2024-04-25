from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 바로 user model을 작성하지 않더라도,
    # 이후 유저 모델 커스텀을 위해서 미리 작성
    pass

class Post(models.Model):
     number = models.AutoField(db_column='번호', primary_key=True)
     title = models.CharField(blank=True, db_column='제목', max_length=10)
     content = models.TextField(blank=True, db_column='내용')
     writer = models.CharField(blank=True, db_column='글쓴이', max_length=10)
     days = models.DateTimeField(db_column='작성일', auto_now_add=True)
     count = models.IntegerField(db_column='조회', default=0)

#     class Meta:
#         managed = True
#         db_table = 'post'

    #  def __str__(self):
    #      return self.title