from django.contrib import admin
from . models import Question,Option,Survey,Responses
# ,Employee

# Register your models here.

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Survey)
admin.site.register(Responses)
# admin.site.register(Employee)
