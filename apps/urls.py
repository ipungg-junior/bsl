from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.views import Landing

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    # path('', Landing.as_view(context=''), name='landing'),
    path('', Landing.as_view(context=''), name='dashboard'),
    path('login/', Landing.as_view(context=''), name='login'),
    path('logout/', Landing.as_view(context=''), name='logout'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
