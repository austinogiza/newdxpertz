# Generated by Django 3.0.3 on 2020-03-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxpert', '0003_auto_20200324_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
