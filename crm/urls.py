from django.urls import path
from django.conf import settings
from crm.views import Relations

handler404 = 'apps.views.entry_not_found'
app_name = 'crm'

urlpatterns = [
    path('relations/', Relations.as_view(context='relations'), name='relations'),
] 
