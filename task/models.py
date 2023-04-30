from django.db import models
from user.models import MyUser




class PROJECT(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class TASK(models.Model):
    project = models.ForeignKey(PROJECT, on_delete=models.CASCADE)
    task    = models.CharField(max_length=255, blank=False, null=False)
    user    = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_done    = models.BooleanField(default = False)
    admin_done    = models.BooleanField(default = False)

    def __str__(self):
        return self.project.name + '-' + str(self.id)