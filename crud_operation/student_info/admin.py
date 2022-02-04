from django.contrib import admin
from student_info.models import Student

# Register your models here.

class Studentlist(admin.ModelAdmin):
     list_display=['name','email','std','sec']




admin.site.register(Student , Studentlist)
