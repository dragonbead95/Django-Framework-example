from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="등록시간")

    # 파이썬에는 클래스가 문자열로 변환되었을때 어떻게 할지 설정할수 있다.
    def __str__(self):
        return self.name

    class Meta:
        db_table = "fastcampus_tag"
        verbose_name = "패스트캠퍼스 태그"
        verbose_name_plural = "패스트캠퍼스 태그"
