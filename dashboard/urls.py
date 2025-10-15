from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects/', views.projects_list, name='projects'),
    path('finance/', views.finance_summary, name='finance'),
    path('settings/', views.settings_view, name='settings'),
    path('refresh/', views.refresh_data, name='refresh_data'),
]