# Generated by Django 3.0.6 on 2020-07-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0007_auto_20200722_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(max_length=20),
        ),
    ]
