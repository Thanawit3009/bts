from django.urls import path, include
from .views import CourseListView,CourseDeleteView

urlpatterns = [
    path("course/", CourseListView.as_view(),name="course_list"),
    path("course/delete/<str:pk>",CourseDeleteView.as_view(),name="delete_course"),

]