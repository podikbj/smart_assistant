# Generated by Django 3.2.13 on 2022-07-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220727_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images_blog/%Y/%m/%d/'),
        ),
    ]
