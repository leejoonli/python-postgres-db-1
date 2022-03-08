# Generated by Django 4.0.3 on 2022-03-08 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_postgres_exercise_1', '0007_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=35)),
                ('min_salary', models.IntegerField()),
                ('max_salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=20)),
                ('hire_date', models.DateField(auto_now_add=True)),
                ('salary', models.IntegerField()),
                ('manager_id', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='python_postgres_exercise_1.department')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='python_postgres_exercise_1.job')),
            ],
        ),
    ]