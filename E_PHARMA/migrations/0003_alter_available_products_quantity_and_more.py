# Generated by Django 4.0.1 on 2023-10-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_PHARMA', '0002_customer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_products',
            name='Quantity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pin',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='Pin',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ordersub',
            name='Quantity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='Price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='Quantity',
            field=models.CharField(max_length=100),
        ),
    ]