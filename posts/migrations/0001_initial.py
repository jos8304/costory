# Generated by Django 4.2.10 on 2024-04-05 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('dt_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('dt_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
            ],
        ),
    ]
