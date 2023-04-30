from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate
from rest_framework.permissions import BasePermission
from .serializers import LoginSerializer, UserCreateSerializer, UserListSerializer
from .models import MyUser



class UserCreateApi(CreateAPIView):
    serializer_class   = UserCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    

@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.data['username']
            password = serializer.data['password']
            username = MyUser.objects.get(email=user_name).username
            user = authenticate(username=username, password=password)
            if user :
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else :
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





class IsSuper(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
    

class UserListApi(ListAPIView):
    serializer_class = UserListSerializer
    query_set = MyUser.objects.all()

    permission_classes = [IsSuper]



