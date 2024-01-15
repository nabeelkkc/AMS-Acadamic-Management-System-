# Generated by Django 4.2.8 on 2023-12-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0002_academicdepartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=100)),
                ('designation_code', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
