from django.urls import path
from patchpanel import views


urlpatterns = [
    path('getpatchInfo/', views.HypervisorVMPatchInfo.as_view()),
    path('', views.HypervisorVMPatch), #dashboard
    path('sendpatchinfo', views.sendpatchinfo),
]
