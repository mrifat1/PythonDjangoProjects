from django.views.generic import ListView
from .models import post

class blogpostview(ListView):
    model = post
    template_name = 'home.html'



