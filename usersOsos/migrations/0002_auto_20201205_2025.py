# Generated by Django 3.1.3 on 2020-12-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersOsos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
