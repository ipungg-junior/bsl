from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=100, null=False)
    # to = models.ForeignKey(Department, on_delete=models.CASCADE)