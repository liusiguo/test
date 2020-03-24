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


class User(models.Model):
    SEX_CHOIES = [
        [0, "男"],
        [1, "女"],
    ]
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, null=True, default=None)
    sex = models.IntegerField(choices=SEX_CHOIES, default=0)
    icon = models.ImageField(upload_to='icon', default='icon/default.jpg')

    class Meta:
        db_table = "t_user"
        verbose_name = 'USer'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
