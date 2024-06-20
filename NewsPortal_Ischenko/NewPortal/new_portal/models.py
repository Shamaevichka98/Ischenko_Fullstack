from django.db import models
# from django.core.validators import MinValueValidator



class Post(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
    )
    description = models.TextField(default='Без описания')
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    date_creation = models.DateTimeField()

    # def __str__(self):
    #     return f'{self.name.title()} {self.description}'


class Category(models.Model):
    name_cat = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()