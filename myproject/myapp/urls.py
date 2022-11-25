from django.urls import path
from . import views

urlpatterns = [
    path('register',views.RegsiterView,name='register' ),

]
