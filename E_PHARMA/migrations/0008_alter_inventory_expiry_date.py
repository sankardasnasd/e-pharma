# Generated by Django 4.0.1 on 2023-10-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_PHARMA', '0007_alter_inventory_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Expiry_Date',
            field=models.CharField(max_length=100),
        ),
    ]
