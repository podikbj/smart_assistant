# Generated by Django 3.2.13 on 2022-07-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20220708_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='Python', max_length=255),
        ),
    ]
