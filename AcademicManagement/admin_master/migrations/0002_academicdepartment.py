# Generated by Django 4.2.8 on 2023-12-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_code', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]