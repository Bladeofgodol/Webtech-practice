from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    title = models.CharField(max_length=23)
    def __str__(self) -> str:
        return self.title
class Post(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField()
    image = models.ImageField()
    Catagory = models.ForeignKey("Catagory", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
# Create your models here.

    def __str__(self) -> str:
        return self.title
