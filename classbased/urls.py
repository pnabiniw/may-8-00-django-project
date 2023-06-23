from django.urls import path
from .views import FirstView, ClassRoomView, ClassRoomTemplateView, StudentListView, StudentDetailView, \
ClassRoomFormView, classroom_form

urlpatterns = [
    path("classroom/", ClassRoomView.as_view(), name="classroom_view"),
    path("classroom-template/", ClassRoomTemplateView.as_view(), name="classroom_template_view"),
    path("student-list/", StudentListView.as_view(), name="student_list_view"),
    path("student-detail/<int:pk>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("classroom-django-form/", ClassRoomFormView.as_view(), name="classroom_django_form"),
    path("classroom-form/", classroom_form, name="classroom_form"),
    path("", FirstView.as_view(), name="first_view")
]
