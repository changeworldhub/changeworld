# Generated by Django 2.2.6 on 2019-11-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0002_auto_20191101_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]