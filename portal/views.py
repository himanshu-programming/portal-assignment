from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from portal.models import Course, Enrollment, Question
from portal.serializers import CourseSerializer, CourseEnrollmentSerializer


# Create your views here.


class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseEnrollment(CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer




