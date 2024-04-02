from django.db import models



# Create your models here.
class Company(models.Model):
    LEGAL_CHOICES = [
        ('1', 'Perorangan'),
        ('2', 'CV'),
        ('3', 'PT'),
        ('4', 'YAYASAN/FIRMA'),
        ('5', 'PT PERORANGAN'),
    ]
    idCompany = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    legal = models.CharField(max_length=40, choices=LEGAL_CHOICES, null=True, blank=True)
    status = models.BooleanField(default=True)


    def set_legal(self, id:int):
        self.legal = self.LEGAL_CHOICES[id][1]
        self.save()

    def __str__(self):
        return self.name

class ContactPerson(models.Model):
    TYPE_CHOICES = [
        ('1', 'Supplier'),
        ('2', 'Customer'),
        ('3', 'Agen'),
        ('4', 'Distributor'),
    ]
    name = models.CharField(max_length=35, null=False)
    phone_number = models.CharField(max_length=13, null=False, unique=True)
    email = models.EmailField(null=True, blank=True)
    legal = models.CharField(max_length=40, choices=TYPE_CHOICES, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name='contacts', null=True)

    def set_legal(self, id:int):
        self.legal = self.TYPE_CHOICES[id][1]
        self.save()
    
    def __str__(self):
        return self.name