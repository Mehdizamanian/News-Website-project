# Generated by Django 4.2.15 on 2024-10-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_contact_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
