# Generated by Django 4.2.6 on 2023-10-23 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_payments_url_session_checkout_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='url_session_checkout_id',
            new_name='url_session_checkout',
        ),
    ]