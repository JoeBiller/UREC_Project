# Generated by Django 4.1.2 on 2022-11-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urec_app', '0002_accidentticket_alter_accident_accident_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='accident_description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='accident',
            name='accident_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='accident',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]
