# Generated by Django 4.0.3 on 2022-03-28 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_id',
        ),
    ]
