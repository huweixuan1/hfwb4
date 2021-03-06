# Generated by Django 2.0.5 on 2018-08-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0014_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='images',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
    ]
