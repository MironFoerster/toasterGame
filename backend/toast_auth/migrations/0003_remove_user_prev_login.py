# Generated by Django 4.2.4 on 2023-09-02 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toast_auth', '0002_alter_user_prev_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='prev_login',
        ),
    ]
