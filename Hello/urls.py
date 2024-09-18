from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('MyApp/', include('MyApp.urls')),
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
