# Generated by Django 4.1.3 on 2023-03-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_entry_sms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='entry',
            name='sms',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='entry',
            name='subject',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]