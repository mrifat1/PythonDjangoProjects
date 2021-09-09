from django.urls import path
from .views import blogpostview,blogdetailview

urlpatterns = [
    path('post/<int:pk>/', blogdetailview.as_view(), name='post_detail'),
    path('',blogpostview.as_view(),name = 'home'),


]