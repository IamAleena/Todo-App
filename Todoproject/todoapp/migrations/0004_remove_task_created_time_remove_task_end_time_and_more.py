# Generated by Django 4.0 on 2022-05-17 04:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_delete_login_delete_register_remove_task_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
