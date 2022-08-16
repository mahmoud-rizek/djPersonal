from django.db import models

# Create your models here.
class about(models.Model):
    blogName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    subTitle = models.TextField(max_length=500)
    aboutme = models.TextField(max_length=10000)
    tw_link = models.URLField()
    github_link = models.URLField()
    lk_in_link = models.URLField()