from django.urls import include, path
from .views import * 

urlpatterns = [
path('ContactForm/',ContactFormList.as_view(),name='ContactFormList'),
path('CatelogRequest/',CatelogRequestList.as_view(),name='CatelogRequestList'),
]


