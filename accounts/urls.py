from django.urls import path
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register-user'),
    path('login', obtain_auth_token),
]

