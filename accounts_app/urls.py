from django.urls import path

from .import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

 
app_name = "accounts_app"
urlpatterns=[
    path('register/', views.UserRegisterView.as_view()),
    path('api_token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='obtain_pair_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


router = routers.SimpleRouter()

router.register('user', views.UserViewSet)
urlpatterns += router.urls
