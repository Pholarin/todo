# Generated by Django 2.2.4 on 2020-03-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200317_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todouser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='todouser',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
