# Generated by Django 4.2.15 on 2024-10-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(to='news.tag'),
        ),
    ]
