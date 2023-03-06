from django.urls import path
from . import views

urlpatterns = [
     path('', views.BandsList.as_view())
]
