from django.contrib import admin
from django.urls import path, include # added
urlpatterns = [
    path('', include('films.urls')), # added
    path('admin/', admin.site.urls),
]