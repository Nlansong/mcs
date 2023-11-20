from django.urls import path
from . import views


app_name = 'ministry'


urlpatterns = [
    path('church-profile/', views.church_profile, name='church_profile' ),
    path('departments/', views.department_list, name='departments'),
    path('departments/<int:pk>/', views.dep_detail, name='dep_detail'),
    path('cells/', views.cell_list, name='cells'),
    path('cells/<int:pk>/', views.cell_detail, name='cell_detail'),
    path('members/', views.members_list, name='members'),
    path('members/<int:pk>/', views.mem_detail, name='mem_detail'),
    path('active-members/', views.active_members, name='active_members'),
    path('working-members/', views.working_members, name='working_members'),
    path('student-members/', views.student_members, name='student_members'),
    path('new-convert/', views.new_converts, name='new_converts'),
    path('male-members/', views.male_members, name='male_members'),

    
]