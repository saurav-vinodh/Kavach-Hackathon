# Generated by Django 4.1.3 on 2023-03-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('contact', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('risk_score', models.IntegerField()),
                ('spam', models.IntegerField()),
            ],
            options={
                'unique_together': {('userid', 'contact')},
            },
        ),
    ]
