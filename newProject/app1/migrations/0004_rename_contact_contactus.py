# Generated by Django 3.2.3 on 2021-05-24 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210524_2330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='ContactUs',
        ),
    ]