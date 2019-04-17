# Generated by Django 2.1.4 on 2019-01-26 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190117_0100'),
        ('code_app', '0002_exercises'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer_is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='exercises',
            name='result',
            field=models.CharField(max_length=5000),
        ),
        migrations.AddField(
            model_name='userexercises',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_app.Exercises'),
        ),
        migrations.AddField(
            model_name='userexercises',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]