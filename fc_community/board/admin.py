from django.contrib import admin
from .models import Board
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ("title",)  # 모델 클래스 안에 있는 필드들이 출력된다.


admin.site.register(Board, BoardAdmin)
