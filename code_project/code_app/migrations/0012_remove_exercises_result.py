# Generated by Django 2.1.4 on 2019-01-27 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_app', '0011_auto_20190127_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='result',
        ),
    ]
