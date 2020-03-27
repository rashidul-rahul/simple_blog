from django.urls import path
from posts.views import post
from .views import save_subsciber, categories


app_name = "blog"

urlpatterns = [
    path("subscribe/", save_subsciber, name="subscribe"),
    path("post/<id>/", post, name="post"),
]