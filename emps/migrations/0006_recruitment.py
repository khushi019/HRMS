# Generated by Django 5.0.7 on 2024-07-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0005_alter_attendance_date_alter_attendance_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('degree', models.CharField(choices=[('BCA', 'BCA'), ('BTECH', 'BTECH'), ('MCA', 'MCA'), ('MBA', 'MBA')], max_length=10)),
            ],
        ),
    ]
