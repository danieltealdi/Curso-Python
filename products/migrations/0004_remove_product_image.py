# Generated by Django 3.2.11 on 2022-03-13 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]