from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns=[
    
    url('^$',views.index,name='index'),
    url(r'^alert/$', views.alert, name='alert'),
    url(r'^gallery/$', views.gallery, name='gallery'),
 


   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)