# Generated by Django 3.1.3 on 2020-12-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxOsos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='receiver_mail_id',
            new_name='receiver_mail',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender_mail_id',
            new_name='sender_mail',
        ),
    ]
