# Generated by Django 4.2.6 on 2023-10-23 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_remove_payments_url_session_checkout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='url_session_checkout_id',
        ),
    ]
