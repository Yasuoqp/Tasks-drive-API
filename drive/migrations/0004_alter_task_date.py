# Generated by Django 5.0.1 on 2024-02-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0003_task_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
