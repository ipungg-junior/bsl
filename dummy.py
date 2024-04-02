import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsl.settings')
application = get_wsgi_application()


from merchandise import models as mdModel
from warehouse import models as warehouseModel
from crm import models as crmModel

class UnitTest:

    def __init__(self):
        self.test_function()

    def test_function(self):
        data = warehouseModel.Inventory.objects.get(product_code='TPB01')
        list_company = crmModel.Company.objects.all()
        list_company[0].set_legal(1)
        data.sender = f'{list_company[0].name} ({list_company[0].legal})'
        data.save()
        print(data.sender)