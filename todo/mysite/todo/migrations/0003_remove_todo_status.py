# Generated by Django 2.0.1 on 2018-11-11 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
    ]