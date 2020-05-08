# Generated by Django 3.0.6 on 2020-05-07 22:31

from django.db import migrations, models
import django.db.models.deletion

def create_type(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Type = apps.get_model('captain_console', 'ProductType')
    type = Type()
    type.id = 0
    type.name = 'Type'
    type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('captain_console', '0011_merge_20200507_2219'),
    ]

    operations = [

        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Type', max_length=255)),
            ],
        ),
        migrations.RunPython(create_type),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='captain_console.ProductType'),
        )
    ]
