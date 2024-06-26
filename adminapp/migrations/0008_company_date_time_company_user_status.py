# Generated by Django 4.2.7 on 2024-02-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_company_last_login_date_company_last_login_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='date_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='user_status',
            field=models.TextField(default='pending', max_length=50, null=True),
        ),
    ]
