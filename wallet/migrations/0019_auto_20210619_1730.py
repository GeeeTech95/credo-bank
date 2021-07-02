# Generated by Django 3.0.5 on 2021-06-20 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0018_auto_20210619_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Failed', 'Failed'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Successful', 'Successful')], max_length=10),
        ),
    ]