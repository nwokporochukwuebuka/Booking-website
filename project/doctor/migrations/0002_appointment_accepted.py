# Generated by Django 4.0.2 on 2022-03-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]