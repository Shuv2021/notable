from django.db import models
from django.contrib.auth.models import User
import json


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    details = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_owner')
    # members = models.CharField(max_length=500)
    members = models.ManyToManyField(User)
    profile_photo = models.CharField(max_length=200, default='/static/media/project-logos/1.png')

    # def get_members(self):
    #     return json.loads(self.members)


class Team(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_owner')
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(User)

    class Meta:
        pass


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    assigned_to = models.ManyToManyField(User)
    status_choices = (
        ('T', 'To Do'),
        ('D', 'Doing'),
        ('I', 'In Test'),
        ('O', 'Done'),
        ('B', 'Blocked'),
        ('L', 'Deleted')
    )
    status = models.CharField(max_length=1, choices=status_choices)
    start_time = models.DateField(null=True)
    end_time = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
