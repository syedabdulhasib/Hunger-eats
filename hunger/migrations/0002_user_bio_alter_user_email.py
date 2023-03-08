# Generated by Django 4.1.2 on 2022-11-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]