# Generated by Django 5.0.6 on 2024-06-24 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_stickynote_is_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stickynote',
            name='date_updated',
        ),
    ]
