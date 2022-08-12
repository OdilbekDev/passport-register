from django.urls import path
from .views import *
urlpatterns = [
    path('index/', Index, name="index"),
    path('about/', About, name="about"),
    path('application/', Send_Application, name="send-application"),
    path('application/migration/', Send_Application_migration, name="Send_Application_migration"),
    path('application/create/', Create_Application, name="create-application"),
    path('application/migration/create/', Create_Application_Migration, name="application_migration"),
    path('application/create/migration/older/', Create_Application_Migration_Older, name="application_migration_old"),
    path('navbat', navbat),
    path('detail', detail),
    path('faq', View_Queue)
]
