# Generated by Django 5.0.1 on 2024-01-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_meta_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='room_id',
            new_name='room',
        ),
    ]
