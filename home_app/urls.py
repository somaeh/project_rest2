
from django.urls import path
from .import views

app_name = 'home_app'
urlpatterns = [
    path('', views.Home.as_view(),  name="home" ),
    path('question/', views.QuestionView.as_view()),
]