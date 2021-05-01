from django.contrib import admin
from django.urls import path,include

from . import settings
from Doctor import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include("Doctor.urls")),
    #path('testview/', views.testview, name='testview'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)