# Generated by Django 3.0.3 on 2020-09-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200924_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
