# Generated by Django 3.0.5 on 2023-11-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0017_auto_20231025_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='bic',
        ),
        migrations.AlterField(
            model_name='demoaccountdetails',
            name='account_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='demoaccountdetails',
            name='iban',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='demoaccountdetails',
            name='swift_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('failed', 'failed'), ('pending', 'pending'), ('processing', 'processing'), ('successful', 'successful')], default='failed', max_length=10),
        ),
    ]