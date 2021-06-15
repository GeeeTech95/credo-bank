# Generated by Django 3.0.5 on 2021-06-14 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0014_transaction_failure_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='currency',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='wallets', to='wallet.Currency'),
            preserve_default=False,
        ),
    ]
