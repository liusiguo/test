from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "t_book"
        verbose_name = 'BOOK'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
