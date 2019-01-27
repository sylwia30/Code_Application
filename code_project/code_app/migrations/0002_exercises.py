# Generated by Django 2.1.4 on 2019-01-26 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=1000)),
                ('date_add_exercise', models.DateTimeField(auto_now_add=True)),
                ('id_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_id', to='code_app.Languages')),
                ('id_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_id', to='code_app.Languages')),
            ],
        ),
    ]
