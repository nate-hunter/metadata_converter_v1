# Generated by Django 3.0.8 on 2020-07-20 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
    ]