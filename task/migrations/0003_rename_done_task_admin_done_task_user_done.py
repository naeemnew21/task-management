# Generated by Django 4.2 on 2023-04-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='done',
            new_name='admin_done',
        ),
        migrations.AddField(
            model_name='task',
            name='user_done',
            field=models.BooleanField(default=False),
        ),
    ]