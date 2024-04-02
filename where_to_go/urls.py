from django.conf import settings
from django.conf.urls.static import static
from main_site.views import home
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
