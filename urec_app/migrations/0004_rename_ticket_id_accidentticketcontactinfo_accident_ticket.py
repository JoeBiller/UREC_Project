# Generated by Django 4.1.2 on 2022-11-30 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urec_app', '0003_alter_accident_accident_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accidentticketcontactinfo',
            old_name='ticket_id',
            new_name='accident_ticket',
        ),
    ]
