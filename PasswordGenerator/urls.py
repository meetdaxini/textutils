from django.contrib import admin
from django.urls import path
from .views import passGen, passHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', passHome, name='pass-home'),
    path('generated', passGen, name='pass-gen'),

]
