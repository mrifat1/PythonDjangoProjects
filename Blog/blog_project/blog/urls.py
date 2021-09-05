from django.urls import path
from .views import blogpostview

urlpatterns = [
    path('',blogpostview.as_view(),name = 'home'),
]