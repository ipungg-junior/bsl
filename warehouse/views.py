from django.shortcuts import render, redirect
from django.views import View
from warehouse.service import _inventory

inv_service = _inventory.InventoryService()
namespace_app = 'Warehouse'

# Create your views here.
class Inbound(View):
    
    context = ''

    def post(self, request, product_code=''):
        _form = request.POST.dict()
        inv_service.update_or_create(_form)
        return redirect(to='warehouse:warehouse-inbound')

    def get(self, request, product_code=''):

        if (self.context == 'inventory-edit'):
            item = inv_service.get_item(product_code)
            return render(request, 'inventori_edit.html', 
                      context={'item': item, 'namespace_app': namespace_app})


        system_info = True
        system_info_content = 'Informasi penting untuk seluruh karyawan yang masih belum submit laporan harian tanggal 21, segera lakukan konfirmasi dengan Administrator.'
        return render(request, 'warehouse_inbound.html', 
                      context={
                          'system_info': system_info, 
                          'system_info_content': system_info_content, 
                          'namespace_app': namespace_app, 
                          'location_choice': inv_service.location_options(),
                          'data_warehouse': inv_service.get_all()
                          })
    