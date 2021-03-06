from django.urls import path

from . import views as app_views
from admin_panel import views as admin_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',admin_views.admin,name='index'),
    path('admin',admin_views.admin,name='admin'),
    path('add_office',admin_views.add_office,name='add_office'),
    path('add_country',admin_views.add_country,name='add_country'),
    path('signup/',app_views.signup,name='signup'),
    path('accounts/login/',app_views.login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'admin/admin.html'),name='logout'),

]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)