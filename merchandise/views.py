from django.shortcuts import render, redirect
from django.views import View
from merchandise.models import SoCModel

# Create your views here.
# Create your views here.
class SoC(View):
    
    context = ''

    def post(self, request):
        _form = request.POST.dict()
        print(_form)
        return redirect(to='merchandise:merchandise-soc')

    def get(self, request):
        system_info = True
        system_info_content = 'Informasi penting untuk seluruh karyawan yang masih belum submit laporan harian tanggal 21, segera lakukan konfirmasi dengan Administrator.'
        _obj = SoCModel.objects.all()
        return render(request, 'merchandise_soc.html', context={'system_info': system_info, 'system_info_content': system_info_content, 'soc_document': _obj})
    

class Sample(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'merchandise_sample.html')
    

class BoM(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'merchandise_wo.html')
    

class WorkOrder(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'merchandise_wo.html')