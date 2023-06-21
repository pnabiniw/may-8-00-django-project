from django.contrib import admin
from .models import Student, ClassRoom, Article, Publication

# Register your models here.
admin.site.register(Student)
admin.site.register(ClassRoom)
admin.site.register(Article)
admin.site.register(Publication)
