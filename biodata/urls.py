from django.urls import path
from . import views

urlpatterns=[
    path('home',views.biodata_home,name="home")
]