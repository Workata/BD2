# Generated by Django 3.1.3 on 2020-12-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classesOsos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='class_id',
            new_name='clasS',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
