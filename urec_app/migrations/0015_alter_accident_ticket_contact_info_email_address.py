# Generated by Django 4.1.2 on 2022-12-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urec_app', '0014_alter_accident_ticket_injury_care_provided_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident_ticket_contact_info',
            name='email_address',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
