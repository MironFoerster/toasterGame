# Generated by Django 4.2.4 on 2023-08-14 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('frequency', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.item')),
                ('killer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='killer_quests', to=settings.AUTH_USER_MODEL)),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='victim_quests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PendingBan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='Keine Begründung.')),
                ('pro', models.IntegerField(default=0)),
                ('con', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.item')),
            ],
        ),
    ]
