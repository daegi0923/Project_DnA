# Generated by Django 4.2.13 on 2024-05-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnceDictNm', models.CharField(max_length=200)),
                ('ksdFnceDictDescContent', models.CharField(max_length=4000)),
            ],
        ),
    ]
