from django.contrib import admin
from .models import Tag
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)  # 모델 클래스 안에 있는 필드들이 출력된다.


admin.site.register(Tag, TagAdmin)
