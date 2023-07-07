from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import hello_world, UserView, StudentView, \
    UserListView, StudentListView, ClassRoomView, ClassRoomListCreateView, StudentAPIView,\
    StudentGenericListView, StudentGenericCreateView, StudentListCreateView, StudentRetrieveView, \
    StudentUpdateView, StudentDeleteView, StudentRetrieveUpdateDeleteView, StudentViewSet

router = DefaultRouter()
router.register('student-viewset', StudentViewSet, basename="student")

urlpatterns = [
    # path("student/", StudentView.as_view()),
    # path("student-list/", StudentListView.as_view()),
    path("user-list/", UserListView.as_view()),
    path("user/", UserView.as_view()),
    path("student/", StudentView.as_view()),
    path("student-api/", StudentAPIView.as_view()),
    path("student-generic-list/", StudentGenericListView.as_view()),
    path("student-generic-create/", StudentGenericCreateView.as_view()),
    path("student-list-create/", StudentListCreateView.as_view()),
    path("classroom/<int:id>/", ClassRoomView.as_view()),
    path("classroom/", ClassRoomListCreateView.as_view()),
    path("hello-world/", hello_world),

    path("student/<int:pk>/", StudentRetrieveView.as_view()),
    path("student-update/<int:pk>/", StudentUpdateView.as_view()),
    path("student-delete/<int:pk>/", StudentDeleteView.as_view()),
    path("student-retrieve-update-delete/", StudentRetrieveUpdateDeleteView.as_view())
] + router.urls


"""
These are non-object levels
list
create

# These are in object levels
retrieve
update
destroy
"""