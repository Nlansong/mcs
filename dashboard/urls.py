from django.urls import path
from . import views
from ministry.views import church_profile

app_name = 'dashboard'


urlpatterns = [
    path('', views.index, name='index'),
    
]