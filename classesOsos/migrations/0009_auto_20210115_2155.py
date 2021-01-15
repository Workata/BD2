# Generated by Django 3.1.4 on 2021-01-15 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachersOsos', '0005_teacher_user'),
        ('classesOsos', '0008_auto_20210102_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachersOsos.teacher'),
        ),
    ]