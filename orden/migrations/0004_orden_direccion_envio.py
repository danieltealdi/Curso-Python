# Generated by Django 3.2.11 on 2022-04-24 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DirEnvio', '0001_initial'),
        ('orden', '0003_alter_orden_envio_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='direccion_envio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DirEnvio.direccionenvio'),
        ),
    ]