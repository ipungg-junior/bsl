from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout



def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)

# Create your views here.
class Landing(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'dashboard.html')
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class Supervisor(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        
        if (self.context == 'dashboard'):
            usage = utils.analyze_system_storage()
            return render(request, 'dashboard.html', context={'usage': usage})
        
        if (self.context == 'dashboard-support'):
            _t = _database.SupportTicket().get_all()
            paginator = Paginator(_t, 20)
            num = request.GET.get("page")
            page_obj = paginator.get_page(num)
            return render(request, 'dashboard-support.html', context={'list_ticket': page_obj})
        


class Account(View):

    context = ''

    def get(self, request):
        if (self.context == 'logout'):
            logout(request)
            return redirect('/login/')
        return render(request, 'sign-in.html')

    def post(self, request):
        if (self.context == 'login'):
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if(user is not None):
                try:
                    login(request, user)
                    return redirect('dashboard')
                except:
                    return JsonResponse({'status': 500, 'url_dest': '/login/', 'info': 'Internal Server Error'})
            else:
                return JsonResponse({'status': 400, 'url_dest': '/login/', 'info': 'Username atau Password salah'})


    
class ToS(View):
    
    context = ''

    def get(self, request):
        return render(request, 'TOS.html')


class Maps(View):
    
    context = ''

    def get(self, request):
        return render(request, 'maps.html')
