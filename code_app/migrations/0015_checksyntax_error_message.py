# Generated by Django 2.1.4 on 2019-01-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_app', '0014_auto_20190127_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='checksyntax',
            name='error_message',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]