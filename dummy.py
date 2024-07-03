import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsl.settings')
application = get_wsgi_application()


from merchandise import models as mdModel
from warehouse import models as warehouseModel
from crm import models as crmModel
from warehouse.service import _inventory
from crm.service import company

class UnitTest:

    def __init__(self):
        self.test_function()

    def test_function(self):
        comp = crmModel.Company.objects.get(idCompany='1322024')
        inv_service = _inventory.InventoryService()
        item = warehouseModel.Inventory.objects.get(product_code='KTN002')
        item.sender = comp.name + ' ' + comp.legal
        item.save()
        item = inv_service.get_item('KTN002')
        com = company.CompanyService()
        ar = com.setup_company_dictionary(40)
        print(ar)