from rest_framework import serializers
from .models import PROJECT, TASK



class ProjectAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROJECT
        fields = ['name']

    def to_representation(self, instance):
        data    = super().to_representation(instance)
        context = {'id':instance.id}
        data.update(context)
        return data
    


class TaskAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TASK
        fields = ('project', 'task', 'user', 'admin_done')
    
    def to_representation(self, instance):
        data    = super().to_representation(instance)
        context = {'id':instance.id, 'user_done': instance.user_done}
        data.update(context)
        return data


class TaskUpdateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TASK
        fields = ('admin_done',)
    

class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TASK
        fields = ('user_done',)
    
    def to_representation(self, instance):
        data    = super().to_representation(instance)
        context = {
                   'id':instance.id,
                   'project':instance.project.id,
                   'task':instance.task,
                   'user':instance.user.id,
                   'admin_done':instance.admin_done,
                 }
        data.update(context)
        return data
