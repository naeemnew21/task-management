
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.permissions import BasePermission
from .serializers import ProjectAdminSerializer, TaskAdminSerializer, TaskUpdateAdminSerializer, TaskUserSerializer
from user.models import MyUser
from .models import PROJECT, TASK



class IsSuper(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
    


class ProjectCreateAdminApi(CreateAPIView):
    serializer_class   = ProjectAdminSerializer
    permission_classes = [IsSuper]


class ProjectListAdminApi(ListAPIView):
    serializer_class   = ProjectAdminSerializer
    queryset = PROJECT.objects.all()

    permission_classes = [IsSuper]




class TaskCreateAdminApi(CreateAPIView):
    serializer_class   = TaskAdminSerializer
    permission_classes = [IsSuper]

class TaskListAdminApi(ListAPIView):
    serializer_class   = TaskAdminSerializer
    queryset = TASK.objects.all()

    permission_classes = [IsSuper]


class TaskUpdateAdminApi(UpdateAPIView):
    serializer_class   = TaskUpdateAdminSerializer
    queryset = TASK.objects.all()

    permission_classes = [IsSuper]



class TaskListUserApi(ListAPIView):
    serializer_class   = TaskUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user   = self.request.user
        queryset = TASK.objects.filter(user = user)
        return queryset
    


class TaskUpdateUserApi(UpdateAPIView):
    serializer_class   = TaskUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user   = self.request.user
        queryset = TASK.objects.filter(user = user)
        return queryset
    