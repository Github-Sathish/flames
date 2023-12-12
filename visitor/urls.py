from django.urls import path

from . import views

urlpatterns = [
    path('getResult',views.GetResult.as_view(), name = 'getResult'),
    
]