# Generated by Django 5.0.6 on 2024-06-25 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
