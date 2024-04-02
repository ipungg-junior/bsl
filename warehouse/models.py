from django.db import models

class WarehouseToken(models.Model):
    token = models.CharField(max_length=100)
    expired = models.DateField(null=True, blank=True)

# Create your models here.
class Inventory(models.Model):
    CATEGORY_CHOICES = [
        ('0', 'Barang mentah'),
        ('1', 'Barang setengah jadi'),
        ('2', 'Barang Jadi'),
        ('3', 'Barang Aset'),
    ]
    LOCATION_CHOICES = [
        ('0', 'Gudang Utama'),
        ('1', 'Gudang Kedua'),
        ('2', 'Gudang Ketiga'),
        ('3', 'Another'),
    ]

    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=50)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='0')
    unit = models.CharField(max_length=50)
    date_in = models.DateField()
    date_out = models.DateField(null=True, blank=True)
    sender = models.CharField(max_length=255)
    storage_location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='0')
    
    def set_category(self, id:int):
        self.category = self.CATEGORY_CHOICES[id][1]
        self.save()
    
    def set_location(self, id:int):
        self.locaation = self.LOCATION_CHOICES[id][1]
        self.save()
            
    def get_location(self, char):
        ret = {}
        _tmp = []
        for i in self.LOCATION_CHOICES:
            item = {}
            item['id'] = int(i[0])
            item['name'] = i[1]
            _tmp.append(item)
            if (i[0] == str(char)):
                ret['selected'] = {'id':int(i[0]), 'name':i[1]}
        ret['member'] = _tmp
        return ret
    
    def __str__(self):
        return self.product_name + ' - ' + self.category 