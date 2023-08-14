from django.views.generic import ListView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class AuthorListView(ListView):
    model = Post
    template_name = "author.html"
