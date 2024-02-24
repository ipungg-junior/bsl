from django.urls import path
from django.conf import settings
from merchandise.views import SoC, WorkOrder, BoM, Sample

handler404 = 'apps.views.entry_not_found'
app_name = 'merchandise'

urlpatterns = [
    path('soc/', SoC.as_view(context=''), name='merchandise-soc'),
    path('wo/', WorkOrder.as_view(context=''), name='merchandise-wo'),
    path('bom/', BoM.as_view(context=''), name='merchandise-bom'),
    path('sample/', Sample.as_view(context=''), name='merchandise-sample'),
] 
