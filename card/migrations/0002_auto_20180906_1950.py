# Generated by Django 2.0.5 on 2018-09-06 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardinfo',
            old_name='username',
            new_name='name',
        ),
    ]
