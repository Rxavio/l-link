# Generated by Django 3.0.3 on 2020-09-24 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200924_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.JPG', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='receiver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='profiles.Profile'),
        ),
    ]
