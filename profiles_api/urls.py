from django.urls import path
from profiles_api import views


urlpatterns = [
    path('HypervisorConnect/', views.HypervisorConnect.as_view()),
    path('dashboard/', views.dashboard),
    path('dashboard/validate', views.HypervisorConnect.as_view()),
    path('dashboard/delete', views.DeleteHypervisorInfo.as_view()),
]
