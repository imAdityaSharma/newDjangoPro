# Generated by Django 3.2.3 on 2021-05-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='query',
            field=models.TextField(max_length=150, verbose_name='query'),
        ),
    ]
