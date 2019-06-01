from django.contrib import admin
from . models import Question,Option

# Register your models here.

admin.site.register(Question)
admin.site.register(Option)