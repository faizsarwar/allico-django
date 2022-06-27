from django.contrib import admin
from django.urls import path,include

admin.site.site_header='Allico Admin Portal'
admin.site.site_title='Welcome Allico admin panel'
admin.site.index_title='Welcome Allico admin panel'

urlpatterns = [
    path('jet/',include('jet.urls')),
    path('jet/dashboard',include('jet.dashboard.urls','jet-dashboard')),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/v1/',include('contact.urls')),
]
