from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    usr_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ': ' + self.description

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'postid':self.id})

class Coments(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    usr_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pst_id = models.ForeignKey(Post, on_delete=models.CASCADE)


