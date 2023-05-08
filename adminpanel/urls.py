from django.contrib import admin
from django.urls import path, include
from panel.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("panel.urls"))
]

handler404 = pageNotFound