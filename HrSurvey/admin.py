from django.contrib import admin
from . models import Question,Option,Survey

# Register your models here.

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Survey)
