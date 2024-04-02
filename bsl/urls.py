
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('merchandise/', include('merchandise.urls')),
    path('warehouse/', include('warehouse.urls')),
    path('crm/', include('crm.urls'))
]
