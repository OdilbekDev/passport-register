
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('register/', Register),
    path('create-user/', Create_User, name="create-user"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
