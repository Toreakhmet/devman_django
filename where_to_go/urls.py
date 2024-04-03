from django.conf import settings
from django.conf.urls.static import static
from places.views import home,get_place
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path('place/<int:place_id>/', get_place, name='place-place_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
