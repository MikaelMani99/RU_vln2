# Generated by Django 3.0.6 on 2020-05-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captain_console', '0005_auto_20200506_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(),
        ),
    ]