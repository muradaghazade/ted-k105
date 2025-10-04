from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partner_logos/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"