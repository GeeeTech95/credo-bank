# Generated by Django 3.0.5 on 2022-10-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_testtransactiondetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-new_date', '-date']},
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='allowed_to_transact',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='available_balance',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='credit_card_blocked',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='credit_card_blocked_reason',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='disallow_reason',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='is_frozen',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], max_length=10),
        ),
    ]
