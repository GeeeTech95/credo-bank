# Generated by Django 3.0.5 on 2021-07-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0024_auto_20210701_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='new_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]