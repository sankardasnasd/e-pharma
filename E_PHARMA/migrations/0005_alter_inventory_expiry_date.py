# Generated by Django 4.0.1 on 2023-10-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_PHARMA', '0004_rename_pin_customer_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Expiry_Date',
            field=models.CharField(max_length=8),
        ),
    ]
