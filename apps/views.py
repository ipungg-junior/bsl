from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from apps.service import account, ceisa

def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)


@method_decorator(login_required(login_url='login'), name='dispatch')
class Landing(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        if (self.context == 'lobby'):
            return render(request, 'lobby.html', context={})
        if (self.context == ''):
            return render(request, 'dashboard.html')


class Account(View):

    context = ''

    def get(self, request):
        if (self.context == 'register'):
            return render(request, 'register.html')
        if (self.context == 'logout'):
            logout(request)
            return redirect('/login/')
        
        st = account.has_symbol("@myuser")
        print(st)

        return render(request, 'sign-in.html')

    def post(self, request):
        if (self.context == 'login'):
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if(user is not None):
                try:
                    login(request, user)
                    return redirect('lobby')
                except:
                    return JsonResponse({'status': 500, 'url_dest': '/login/', 'info': 'Internal Server Error'})
            else:
                return JsonResponse({'status': 400, 'url_dest': '/login/', 'info': 'Username atau Password salah'})

        if (self.context == 'register'):
            sts, data = account.UserAccount.create(request.POST)
            if (sts is None):
                return render(request, 'register.html', context=data)
            return redirect('/login/')

    
class ToS(View):
    
    context = ''

    def get(self, request):
        return render(request, 'TOS.html')

