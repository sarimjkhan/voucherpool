# Generated by Django 4.0.4 on 2022-05-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucherpool_api', '0003_customer_email_specialoffer_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
