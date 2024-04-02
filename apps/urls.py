from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.views import Landing, Account

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('', Landing.as_view(context='lobby'), name='lobby'),
    path('register/', Account.as_view(context='register'), name='register'),
    path('login/', Account.as_view(context='login'), name='login'),
    path('logout/', Account.as_view(context='logout'), name='logout'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
