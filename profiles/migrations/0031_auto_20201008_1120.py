# Generated by Django 3.0.3 on 2020-10-08 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_auto_20201007_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('YAC', 'TABLE 1'), ('NAC', 'TABLE 2'), ('DEL', 'TABLE 3'), ('KIN', 'TABLE 4'), ('QUE', 'TABLE 5'), ('TAC', 'TABLE 6'), ('MAC', 'TABLE 7'), ('XEL', 'TABLE 8'), ('GIN', 'TABLE 9'), ('WUE', 'TABLE 10'), ('YAK', 'TABLE 11'), ('NOC', 'TABLE 12'), ('DEG', 'TABLE 13'), ('KIT', 'TABLE 14'), ('QUO', 'TABLE 15'), ('GOC', 'TABLE 16'), ('JAC', 'TABLE 17'), ('DAL', 'TABLE 18'), ('KUN', 'TABLE 19'), ('QAE', 'TABLE 20')], max_length=5)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AlterField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Table'),
        ),
    ]
