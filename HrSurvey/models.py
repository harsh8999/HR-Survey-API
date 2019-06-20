from django.db import models

# Create your models here.
class Question(models.Model):
    is_required = models.BooleanField(default=False)
    selected_type = models.CharField(max_length=50)
    question = models.TextField()
    
    
class Option(models.Model):
    option = models.CharField(max_length=500,null=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='options')

class Survey(models.Model):
    title = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    questionID = models.ManyToManyField(Question)
    is_active = models.BooleanField(default = False)

# class Employee(models.Model):
#     name = models.CharField(max_length = 500)
#     company = models.CharField(max_length = 300)
#     department = models.CharField(max_length=500)
#     level = models.IntegerField()
#     dateOfJoining = models.DateField()
#     pastExperience  = models.IntegerField()
#     location = models.TextField()

class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE,related_name='survey_response')

class Responses(models.Model):
    # employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_id')
    survey_response = models.ForeignKey(SurveyResponse, on_delete = models.CASCADE,related_name='survey_response', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='responses')
    option = models.ForeignKey(Option, on_delete=models.CASCADE,related_name='option_id')
    answer = models.TextField()

    @property
    def q_id(this):
        return this.question.id

