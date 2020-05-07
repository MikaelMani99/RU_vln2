# Generated by Django 3.0.6 on 2020-05-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captain_console', '0003_auto_20200506_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='captain_console.Product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]