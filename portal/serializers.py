from rest_framework import serializers
from portal import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class CourseEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Enrollment
        fields = '__all__'
