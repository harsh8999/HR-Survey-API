from rest_framework import serializers
from . models import Question, Option, Survey, Responses, SurveyResponse
from django.contrib.auth.models import User
# , Employee

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option  #model to bind 
        # fields = ('option','question_id')   #fields you want to send in get request
        fields = "__all__"



class QuestionSerializers(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question    #model to bind 
        fields = '__all__'  #fields you want to send in get request
        #fields = ('question',)

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey  #model to bind 
        fields = '__all__'  #fields you want to send in get request

class SpecificSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey  #model to bind 
        fields = '__all__'  #fields you want to send in get request

class ResponsesSerializer(serializers.ModelSerializer):
    # # question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    question = serializers.SlugRelatedField(slug_field='question', read_only=True)
    q_id = serializers.IntegerField()
    
    class Meta:
        model = Responses  #model to bind 
        fields = '__all__'  #fields you want to send in get request
        # fields = ('question','answer')


class SurveyResponsesSerializer(serializers.ModelSerializer):
    survey_response = ResponsesSerializer(many=True, read_only=True)
    class Meta:
        model = SurveyResponse
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'