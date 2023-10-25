# Generated by Django 4.1.7 on 2023-09-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_demoaccountdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('failed', 'failed'), ('pending', 'pending'), ('processing', 'Processing'), ('successful', 'successful')], default='failed', max_length=10),
        ),
    ]