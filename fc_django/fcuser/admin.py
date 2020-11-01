from django.contrib import admin
from .models import Fcuser
# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    # ","를 하지 않으면 문자열 하나로 인식하기 때문에 콤마를 기입해주어야 한다.(튜플로 인식안한다.)
    list_display = ("email",)


# Fcuser 클래스를 지정하고 FcuserAdmin 클래스를 통해서 원하는 필드만 보여준다.
admin.site.register(Fcuser, FcuserAdmin)
