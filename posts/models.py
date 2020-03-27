from django.db import models
from django.urls import reverse
from blog.models import Category, Author


class Post(models.Model):
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    overview = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post", kwargs={
            "id": self.id
        })

