# Generated by Django 3.0.8 on 2020-07-23 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20200722_1840'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='metadata',
            name='studio',
            field=models.CharField(choices=[('A&E', 'A&E'), ('Discovery', 'Discovery'), ('Disney', 'Disney')], max_length=100),
        ),
    ]
