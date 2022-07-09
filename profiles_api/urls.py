from django.urls import path
from profiles_api import views


urlpatterns = [
    path('HypervisorConnect/', views.HypervisorConnect.as_view()),
    path('dashboard/', views.dashboard),
]
