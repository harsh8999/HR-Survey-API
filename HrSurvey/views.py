from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint
from . models import Question, Option,Survey,Responses, SurveyResponse
# , Employee
from . serializers import (OptionSerializer,
                           SpecificSurveySerializer, 
                           SurveySerializer,
                           QuestionSerializers,
                           ResponsesSerializer,
                            UserSerializer,    
                           SurveyResponsesSerializer)
# , EmployeeResponsesSerializer
from itertools import zip_longest
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
            else:
                return Response({'error':'Incorrect Password Provided'}, status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error':'User Does not exist'}, status.HTTP_400_BAD_REQUEST)


class SpecificResponseQuestionList(APIView):
    ###### get request
    def get(self,request,pk):       
        snippet = get_object_or_404(Question, pk=pk)
        serilizer = ResponseQuestionSerializers(snippet)    #sending only one object
        return Response(serilizer.data)

class SpecificSurveyList(APIView):
    ###### get request
    def get(self,request,pk):       
        snippet = get_object_or_404(Survey, pk=pk)
        serilizer = SpecificSurveySerializer(snippet)    #sending only one object
        return Response(serilizer.data)

class RecentList(APIView):
    ###### get request
    def get(self,request):       
        queryset = Question.objects.latest('id')
        serilizer = QuestionSerializers(queryset)    #sending only one object
        return Response(serilizer.data)

class SpecificQuestionList(APIView):
    ###### get request
    def get(self,request,pk):       
        snippet = get_object_or_404(Question, pk=pk)
        serilizer = QuestionSerializers(snippet)    #sending only one object
        return Response(serilizer.data)

    def delete(self,request,pk):
        snippet = get_object_or_404(Question, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        # print(request.data)
        option_new_obj = request.data.pop('options')
        # print(option_new_obj)
        # request.data.pop('id')
        
        serializer = QuestionSerializers(get_object_or_404(Question, pk=pk),data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            
            for old_option, new_option in zip_longest(instance.options.all(), option_new_obj):
                if old_option is not None and new_option is not None:
                    old_option.option = new_option['option']
                    old_option.save()

                elif old_option is None:
                    # questionObj = get_object_or_404(Question, pk=pk)
                    option = {'option':new_option['option']}
                    instance.options.create(**option)
                    instance.save()
            
                elif new_option is None:
                    # questionObj = get_object_or_404(Question, pk=pk)
                    # instance.options.remove(old_option)
                    instance.options.filter(id=old_option.id).delete()
                    instance.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
        
        

####### Create your views here.
class QuestionList(APIView):
    ###### get request
    def get(self,request):       
        queryset = Question.objects.all()
        serilizer = QuestionSerializers(queryset, many=True)
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
            serializer = QuestionSerializers(data=request.data['questionGroup'][i])
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
        

class SurveyList(APIView):
    
    ###### get request
    def get(self,request):       
        queryset = Survey.objects.all()
        serilizer = SurveySerializer(queryset, many=True)    #sending only one object
        return Response(serilizer.data)

    def post(self,request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            survey = serializer.save()
            # survey.survey.create()  #create an instance in IsActive model
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        snippet = get_object_or_404(Survey, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        serializer = SurveySerializer(get_object_or_404(Survey, pk=pk),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)

class ResponsesList(APIView):
    def get(self,request):
        queryset = Response.objects.all()
        serilizer = ResponsesSerializer(queryset, many=True)    #sending only one object
        return Response(serilizer.data)
    
    def post(self,request):
        # print(request.data)

        # {'survey_id': 21, 'employee_id': '1', 
        # 'answers': [{'id': 106, 'question': 74, 'option': 'No'}, 
                   #  {'id': 88, 'question': 56, 'option': '1'}, 
                    # {'id': 116, 'question': 80, 'option': 'Yes'}, 
                    # {'id': '', 'question': '', 'option': ''}, 
                    # {'id': '', 'question': '', 'option': ''}, 
                    # {'id': 122, 'question': 83, 'option': 'coding'}, 
                    # {'id': 123, 'question': 83, 'option': 'swimming '}, 
                    # {'id': 126, 'question': 84, 'option': '4'}]}
        answers = request.data.pop('answers')
        employee = request.data.pop('employee_id')
        survey_response = SurveyResponse.objects.create(**request.data) 
        # answers list
        
        # print(answers)

        for answer in answers.copy():
            if(answer['id'] is '' and answer['question'] is '' and answer['option'] is ''):
                answers.remove(answer)
                # print("answer",answer)  
            else:
                temp = answer['option']
                answer['option'] = answer['id']
                del(answer['id'])
                answer['answer'] = temp
                # answer['survey'] = survey_id
                # answer['employee_id'] = employee_id

        # print("answers",answers)
        
        for answer in answers:
            survey_response.survey_response.create(option_id = answer['option'],answer=answer['answer'],question_id = answer['question'])
            # r.save()
            # return Response("done", status=status.HTTP_201_CREATED)
        return Response("done", status=status.HTTP_201_CREATED)



class SpecificSurveyResponseList(APIView):
    # send survey_id and get its response
    def get(self,request,pk):
        queryset = SurveyResponse.objects.filter(survey_id=pk)
        serilizer = SurveyResponsesSerializer(queryset, many=True)    #sending only one object

        # for i in serilizer.data:
        # print(serilizer.data)
        for data in serilizer.data:
            responses=[]
            responses_completed = []
            for response in  data['survey_response']:
                question = Question.objects.get(id=response['q_id'])
                if question.id in responses_completed:
                    continue
                if(question.selected_type == 'multi_choice'):
                    resps = Responses.objects.filter(question_id=response['q_id'],survey_response_id=response['survey_response'])
                    res = dict(
                        id=[],
                        question=response['question'],
                        q_id=response['q_id'],
                        survey_response=response['survey_response'],
                        answer=[],
                        option=[]
                    )
                    for resp in resps:
                        res['id'].append(resp.id)
                        res['answer'].append(resp.answer)
                        res['option'].append(resp.option.id)
                    responses.append(res)
                    responses_completed.append(question.id)
                else:
                    responses.append(response)
                    responses_completed.append(response['q_id'])
            data['survey_response'] = responses
            # pprint(responses)
        return Response(serilizer.data)
	
##########################

class SpecificSurveyResponseOptionList(APIView):
    # send survey_id and get its response
    def get(self,request,pk,q_id):
        queryset = SurveyResponse.objects.filter(survey_id=pk)
        serilizer = SurveyResponsesSerializer(queryset, many=True)    #sending only one object
        # for i in serilizer.data:
        return Response(serilizer.data)        
#############################
class dataForGraph(APIView):
    def get(self,request,pk,question_id):
        question = Question.objects.get(id=question_id)
        
        # print("question",question)
        data = dict.fromkeys(map(lambda option: option.option, question.options.all()))
        # print(data)
        survey = Survey.objects.get(id=pk)
        # print("survey",survey)
        for key in data.keys():
            data[key] = survey.survey_response.filter(survey_response__question_id=question_id, survey_response__answer=key).count()
        
        return Response(
            [dict(name=key, value=value) for key, value in data.items()],
            status=status.HTTP_200_OK
        )

class ActiveSurveyList(APIView):
    def get(self,request):
        survey = Survey.objects.filter(is_active=True)
        return Response(SurveySerializer(survey,many=True).data,status.HTTP_200_OK)

class SurveyQuestionList(APIView):
    def get(self,request,pk):
        survey = Survey.objects.get(id=pk)
        questions = survey.questionID.all()
        return Response(QuestionSerializers(questions,many=True).data,status.HTTP_200_OK)