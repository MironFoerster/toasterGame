# Generated by Django 4.2.4 on 2023-09-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toast_auth', '0005_alter_user_prev_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prev_login',
            field=models.DateTimeField(null=True),
        ),
    ]