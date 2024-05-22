from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
from accounts.serializers import RegisterSerializer


class RegisterAPIView(ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
