from django.contrib import admin

# Register your models here.

from .models import Course,Section,Quiz,Question,Answer,Video_Module,Link

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Video_Module)
admin.site.register(Link)
