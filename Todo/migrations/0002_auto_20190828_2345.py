# Generated by Django 2.2.4 on 2019-08-28 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]