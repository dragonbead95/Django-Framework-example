from django.contrib import admin
from .models import Fcuser
# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")  # 모델 클래스 안에 있는 필드들이 출력된다.


admin.site.register(Fcuser, FcuserAdmin)
