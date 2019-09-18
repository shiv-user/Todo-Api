from django.db import models

# Create your models here.
class Todo(models.Model):
	todo = models.CharField(max_length=100, null=False)
	done = models.BooleanField(default=False)