# Generated by Django 3.0.5 on 2021-06-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_auto_20210613_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='applied_for_card',
            field=models.BooleanField(default=False),
        ),
    ]