from datetime import datetime

from django.db import models


# Create your models here.
class TaskOwner(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the task owner")
    image_field = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the task")
    description = models.TextField(max_length=1000, help_text="Description of the task")
    created_date = models.DateTimeField(default=datetime.now(), help_text="Date of the created task")
    name = models.ForeignKey(TaskOwner, on_delete=models.CASCADE, help_text="Name of the user")

    def __str__(self):
        return self.title + '  |   ' + self.description + '  |   ' \
               + str(self.created_date)
