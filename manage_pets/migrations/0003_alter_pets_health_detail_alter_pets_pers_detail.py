# Generated by Django 4.2.4 on 2023-08-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_pets', '0002_remove_pets_photos_sec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='health_detail',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pers_detail',
            field=models.TextField(max_length=350),
        ),
    ]
