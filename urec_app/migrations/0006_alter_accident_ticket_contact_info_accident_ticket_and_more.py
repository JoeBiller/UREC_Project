# Generated by Django 4.1.2 on 2022-12-06 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urec_app', '0005_accident_ticket_accident_ticket_injury_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident_ticket_contact_info',
            name='accident_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.accident_ticket'),
        ),
        migrations.AlterField(
            model_name='accident_ticket_injury',
            name='accident_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urec_app.accident_ticket'),
        ),
    ]
