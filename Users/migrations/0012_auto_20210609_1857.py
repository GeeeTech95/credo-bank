# Generated by Django 3.0.5 on 2021-06-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20210609_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
