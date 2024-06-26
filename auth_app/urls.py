from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]