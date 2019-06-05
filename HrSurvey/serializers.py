from rest_framework import serializers
from . models import Question, Option, Survey

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option  #model to bind 
        fields = ('option','question_id')   #fields you want to send in get request



class QuestionSerialiers(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question    #model to bind 
        fields = '__all__'  #fields you want to send in get request
        #fields = ('question',)

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey  #model to bind 
        fields = '__all__'  #fields you want to send in get request


