# Generated by Django 3.0.3 on 2020-10-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_auto_20201007_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='table',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
