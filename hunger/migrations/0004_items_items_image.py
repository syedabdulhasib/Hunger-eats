# Generated by Django 4.1.2 on 2023-03-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='items_image',
            field=models.ImageField(default='base image.jpg', null=True, upload_to=''),
        ),
    ]
