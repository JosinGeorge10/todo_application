# Generated by Django 4.2 on 2023-04-24 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]