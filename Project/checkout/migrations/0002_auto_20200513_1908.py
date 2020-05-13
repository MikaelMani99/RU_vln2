# Generated by Django 3.0.6 on 2020-05-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
