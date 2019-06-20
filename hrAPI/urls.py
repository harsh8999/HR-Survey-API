"""hrAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HrSurvey.views import (QuestionList, 
                            OptionList, 
                            RecentList, 
                            SurveyList, 
                            SpecificSurveyList,
                            SpecificQuestionList, 
                            ResponsesList,
                            dataForGraph,
                            SpecificResponseQuestionList,
                            SpecificSurveyResponseList,
							SpecificSurveyResponseOptionList,
                            Login,
                            ActiveSurveyList,
                            SurveyQuestionList)
                            # SpecificEmployeeResponseList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/',QuestionList.as_view()),
    path('options/',OptionList.as_view()),
    path('recent/',RecentList.as_view()),
    path('survey/',SurveyList.as_view()),
    path('survey/<int:pk>/',SurveyList.as_view()),
    path('specific-survey/<int:pk>/',SpecificSurveyList.as_view()),
    path('question/<int:pk>/',SpecificQuestionList.as_view()),
    path('question-response/<int:pk>/',SpecificResponseQuestionList.as_view()),
    path('response/', ResponsesList.as_view()),
    path('textarea-answers/<int:pk>/<int:q_id>/',SpecificSurveyResponseOptionList.as_view()),
    path('survey-response/<int:pk>/',SpecificSurveyResponseList.as_view()),
    path('graph/<int:pk>/<int:question_id>/',dataForGraph.as_view()),
    path('login/',Login.as_view()),
    path('activeSurvey/',ActiveSurveyList.as_view()),
    path('surveyQuestion/<int:pk>/',SurveyQuestionList.as_view())
]
