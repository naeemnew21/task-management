from django.urls import path
from . import views 
from . import api 

app_name = 'task'



urlpatterns = [

    path('project-create', api.ProjectCreateAdminApi.as_view(), name = 'project-create'),
    path('project-list', api.ProjectListAdminApi.as_view(), name = 'project-list'),
    path('task-create', api.TaskCreateAdminApi.as_view(), name = 'task-create'),
    path('task-list', api.TaskListAdminApi.as_view(), name = 'task-list'),
    path('task-update/<int:pk>', api.TaskUpdateAdminApi.as_view(), name = 'task-update'),

    path('my-task-list', api.TaskListUserApi.as_view(), name = 'my-task-list'),
    path('my-task-update/<int:pk>', api.TaskUpdateUserApi.as_view(), name = 'my-task-update'),


]
