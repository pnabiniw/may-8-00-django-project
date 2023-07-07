from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from myapp.models import ClassRoom, Student, StudentProfile
from api.serializers import ClassRoomModelSerializer, StudentModelSerializer, StudentProfileSerializer
from .permissions import IsSuperAdmin


class ClassRoomViewSet(ModelViewSet):
    """
    Here actions are list, retrieve, update, destroy, partial_update, create, student
    """
    # permission_classes = [IsSuperAdmin, ]

    def get_permissions(self):
        if self.action == "create":
            return [IsSuperAdmin(), ]
        return [IsAuthenticated(), ]

    def get_queryset(self):
        return ClassRoom.objects.all()

    def get_serializer_class(self):
        if self.action == 'student':
            return StudentModelSerializer
        return ClassRoomModelSerializer

    @action(detail=True)
    def student(self, *args, **kwargs):
        classroom = self.get_object()
        students = Student.objects.filter(classroom=classroom)
        ser = self.get_serializer(students, many=True)
        return Response(ser.data)


class StudentViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action == "profile":
            return StudentProfileSerializer
        return StudentModelSerializer

    @action(detail=True)
    def profile(self, *args, **kwargs):
        student = self.get_object()
        try:
            profile = student.studentprofile
            ser = self.get_serializer(profile)
            return Response(ser.data)
        except:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)


class StudentProfileViewSet(ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
