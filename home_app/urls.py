
from django.urls import path
from .import views

app_name = 'home_app'
urlpatterns = [
    path('', views.Home.as_view(),  name="home" ),
    path('questions/', views.QuestionView.as_view()),
    path('questions/<int:pk>/', views.QuestionView.as_view()),

]