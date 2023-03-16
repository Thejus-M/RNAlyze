from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('analyses/',views.home,name='fun'),
    path('about/',views.about,name='about'),
    
]