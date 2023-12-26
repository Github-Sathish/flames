from django.urls import path

from . import views

urlpatterns = [
    path('getResult/',views.GetResult.as_view() , name = 'getResult'),
    # path('getJoke/', views.GetResult.get_joke, name='get_joke'),  # Add this line
    path('downloadVideo/',views.DownloadVideo.as_view() , name = 'downloadVideo'),
    
]