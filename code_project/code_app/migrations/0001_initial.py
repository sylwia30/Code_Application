# Generated by Django 2.1.4 on 2019-01-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=64)),
                ('nr_section', models.IntegerField(unique=True)),
                ('section', models.CharField(max_length=200)),
                ('date_add_language', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
