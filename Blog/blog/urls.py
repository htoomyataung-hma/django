from django.urls import path
from .views import BlogListView, AuthorListView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("author/", AuthorListView.as_view(), name="author"),
]
