from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Question, Option
from . serializers import QuestionSerialiers, OptionSerializer


class RecentList(APIView):
    
    ###### get request
    def get(self,request):       
        queryset = Question.objects.latest('id')
        serilizer = QuestionSerialiers(queryset)    #sending only one object
        return Response(serilizer.data)

####### Create your views here.
class QuestionList(APIView):
    
    ###### get request
    def get(self,request):       
        queryset = Question.objects.all()
        serilizer = QuestionSerialiers(queryset, many=True)
        return Response(serilizer.data)


    ###### post request
    def post(self,request):
        print("length",len(request.data['questionGroup']))
        print(request.data)
        ### {'questionGroup': [{'question': 'asda', 'is_required': True, 'selected_type': 'textarea', 'optionsGroup': [{'option': 'ds'}]}]}
        question_saved = False
        for i in range(len(request.data['questionGroup'])):
            
            options = request.data['questionGroup'][i].pop('optionsGroup') #save options
        
        #     # save Question
            serializer = QuestionSerialiers(data=request.data['questionGroup'][i])
            if serializer.is_valid():
                question = serializer.save()
                question_saved=True
            # for each option in options
            for option in options:
                question.options.create(**option)

        if question_saved == True:
            return Response("done", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

class OptionList(APIView):
    ###### get request
    def get(self,request):       
        queryset = Option.objects.all()
        serilizer = OptionSerializer(queryset, many=True)
        return Response(serilizer.data)
        