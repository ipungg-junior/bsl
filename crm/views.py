from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from crm.service import contact, company
import requests

namespace_app = 'crm'

def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)


@method_decorator(login_required(login_url='login'), name='dispatch')
class Relations(View):
    
    context = ''

    def post(self, request):
        pass

    def get(self, request):
        if (self.context == 'relations'):
            url = "https://randomuser.me/api/"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                name = data['results'][0]['name']['first'] + data['results'][0]['name']['last']
                phone= data['results'][0]['phone']
                email= data['results'][0]['email']
                contact.create_new(name=name, phone=phone, email=email, legal=0)
            return render(request, 'crm_relations.html', 
                          context={'namespace_app': 'CRM', 
                                   'contact_type': contact.get_contact_type(), 
                                   'contact_list': contact.get_list(), 
                                   'company_list': company.get_list()})