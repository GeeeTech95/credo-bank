# Generated by Django 3.0.5 on 2023-10-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0016_auto_20231025_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date_approved',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='failure_reason',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='is_failed',
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
        migrations.AddField(
            model_name='transaction',
            name='mail_is_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('failed', 'failed'), ('pending', 'pending'), ('processing', 'Processing'), ('successful', 'successful')], default='failed', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
