# Generated by Django 3.2.11 on 2022-03-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='default', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
