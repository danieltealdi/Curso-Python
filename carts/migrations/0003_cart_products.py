# Generated by Django 3.2.11 on 2022-03-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
        ('carts', '0002_auto_20220327_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='carts.CartProduct', to='products.Product'),
        ),
    ]
