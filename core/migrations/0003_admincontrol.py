# Generated by Django 3.0.5 on 2021-06-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210528_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_transactions', models.BooleanField(default=False)),
            ],
        ),
    ]
