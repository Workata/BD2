# Generated by Django 3.1.4 on 2021-01-02 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersOsos', '0004_auto_20201227_1806'),
        ('adminsOsos', '0003_remove_admin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(default='xd', on_delete=django.db.models.deletion.CASCADE, to='usersOsos.user'),
            preserve_default=False,
        ),
    ]
