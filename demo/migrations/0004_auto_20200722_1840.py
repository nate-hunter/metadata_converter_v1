# Generated by Django 3.0.8 on 2020-07-22 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_metadata_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='show',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='studio',
            field=models.CharField(choices=[('A&E', 'A&E'), ('Discovery', 'Discovery'), ('Discovery', 'Discovery')], max_length=100),
        ),
    ]