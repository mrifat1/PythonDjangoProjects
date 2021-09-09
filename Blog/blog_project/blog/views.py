from django.views.generic import ListView,DetailView
from .models import post

class blogpostview(ListView):
    model = post
    template_name = 'home.html'

class blogdetailview(DetailView):
    model = post
    template_name = 'post_detail.html'



