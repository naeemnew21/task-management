from django.urls import path
from . import views 
from . import api

app_name = 'user'


urlpatterns = [
    
    path('login', api.login_api, name = 'login'),
    path('sign-up', api.UserCreateApi.as_view(), name = 'sign-up'),
    path('users', api.UserListApi.as_view(), name = 'users'),

]
