# Generated by Django 3.0.5 on 2023-11-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0020_remove_demoaccountdetails_countr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demoaccountdetails',
            name='country',
            field=models.CharField(max_length=25),
        ),
    ]