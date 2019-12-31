from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shrit_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
