# Generated by Django 4.0.1 on 2023-11-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_PHARMA', '0002_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='Product_Type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
