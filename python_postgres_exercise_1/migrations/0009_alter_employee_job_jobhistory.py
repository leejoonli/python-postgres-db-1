# Generated by Django 4.0.3 on 2022-03-08 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_postgres_exercise_1', '0008_job_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='python_postgres_exercise_1.job'),
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_histories', to='python_postgres_exercise_1.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_histories', to='python_postgres_exercise_1.employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_histories', to='python_postgres_exercise_1.job')),
            ],
        ),
    ]
