# Generated by Django 3.0.7 on 2020-10-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxpert', '0009_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
