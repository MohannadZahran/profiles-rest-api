from django.urls import path, include
from profiles_api import views
from django.contrib import admin

urlpatterns = [
    path('admin'/, admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
