from django.urls import path
from portal import views

urlpatterns = [
    path('courses',views.CourseList.as_view(), name='course-list'),
]
