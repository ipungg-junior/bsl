from django.urls import path
from django.conf import settings
from warehouse.views import Inbound

handler404 = 'apps.views.entry_not_found'
app_name = 'warehouse'

urlpatterns = [
    path('inbound/', Inbound.as_view(context=''), name='warehouse-inbound'),
] 
