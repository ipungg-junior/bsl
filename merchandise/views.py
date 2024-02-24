from django.shortcuts import render
from django.views import View

# Create your views here.
# Create your views here.
class SoC(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'merchandise_soc.html')
    

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