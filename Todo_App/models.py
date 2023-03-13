from django.db import models

# Create your models here.
class Task(models.Model):
    task_id=models.AutoField(primary_key=True)
    task_desc=models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="In Processing")
   