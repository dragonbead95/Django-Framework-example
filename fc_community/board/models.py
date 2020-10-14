from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    # on_delete => 현재 게시글을 작성하였는데 사용자가 정보가 db에서 삭제되면 사용자가 작성한 글도 삭제되는 방식.
    writer = models.ForeignKey("fcuser.Fcuser", on_delete=models.CASCADE,
                               verbose_name="작성자")

    tags = models.ManyToManyField('tag.Tag', verbose_name="태그")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="등록시간")

    # 파이썬에는 클래스가 문자열로 변환되었을때 어떻게 할지 설정할수 있다.
    def __str__(self):
        return self.title

    class Meta:
        db_table = "fastcampus_board"
        verbose_name = "패스트캠퍼스 게시글"
        verbose_name_plural = "패스트캠퍼스 게시글"
