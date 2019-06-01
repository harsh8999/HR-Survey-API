from django.db import models

# Create your models here.
class Question(models.Model):
    
    is_required = models.BooleanField(default=False)
    selected_type = models.CharField(max_length=50)
    question = models.TextField()
    
class Option(models.Model):
    option = models.CharField(max_length=500,null=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='options')