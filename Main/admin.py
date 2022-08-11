from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Slider)
admin.site.register(Application_Citizenship)
admin.site.register(Application_Migration)
admin.site.register(Application_Migration_Older)
admin.site.register(Queue_Citizenship)
admin.site.register(Queue_Migration)
admin.site.register(Service)
admin.site.register(Gallery)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply_Comment)
admin.site.register(Info)