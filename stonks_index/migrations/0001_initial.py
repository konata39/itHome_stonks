# Generated by Django 3.2.7 on 2021-09-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBTest',
            fields=[
                ('test', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
