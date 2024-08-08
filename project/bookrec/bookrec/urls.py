from django.contrib import admin
from django.urls import path, include
from recommendations.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('api/', include('recommendations.urls')),
]
