# Generated by Django 2.0 on 2020-03-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
