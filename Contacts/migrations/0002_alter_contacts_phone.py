# Generated by Django 4.2 on 2023-06-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]