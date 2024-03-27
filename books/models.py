from django.db import models

from django.urls import reverse
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}  ,,by: {self.author.capitalize()}'

    def get_absolute_url(self):
        return reverse('book_detail', args={self.id})
