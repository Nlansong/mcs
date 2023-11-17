from django.urls import path
from . import views


app_name = 'ministry'


urlpatterns = [
    path('church-profile/', views.church_profile, name='church_profile' )
]