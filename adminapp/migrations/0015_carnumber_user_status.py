# Generated by Django 4.2.7 on 2024-02-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_carnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='carnumber',
            name='user_status',
            field=models.CharField(default='Accepted', max_length=50),
        ),
    ]