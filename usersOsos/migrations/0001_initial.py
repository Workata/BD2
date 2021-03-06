# Generated by Django 3.1.3 on 2020-12-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('user_type', models.CharField(choices=[('TEACHER', 'Teacher'), ('STUDENT', 'Student'), ('ADMIN', 'Admin')], max_length=10)),
            ],
        ),
    ]
