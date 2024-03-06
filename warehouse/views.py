from django.shortcuts import render, redirect
from django.views import View


namespace_app = 'Warehouse'

# Create your views here.
class Inbound(View):
    
    context = ''

    def post(self, request):
        _form = request.POST.dict()
        print(_form)
        return redirect(to='warehouse:warehouse-inbound')

    def get(self, request):
        system_info = True
        system_info_content = 'Informasi penting untuk seluruh karyawan yang masih belum submit laporan harian tanggal 21, segera lakukan konfirmasi dengan Administrator.'
        print(system_info_content)
        return render(request, 'warehouse_inbound.html', context={'system_info': system_info, 'system_info_content': system_info_content, 'namespace_app': namespace_app})
    