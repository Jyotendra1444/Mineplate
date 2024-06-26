# Generated by Django 4.2.7 on 2024-02-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_userdetailstwo_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=254)),
                ('employee_count', models.IntegerField()),
                ('company_location', models.CharField(max_length=255)),
                ('document_proof', models.FileField(upload_to='documents/')),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
