from django.db import models

# Create your models here.
class SoCModel(models.Model):
    soc_number = models.CharField(max_length=20, null=False, blank=True)
    po_number = models.CharField(max_length=20, null=False, blank=True)
    customer = models.CharField(max_length=25, null=False, blank=True)
