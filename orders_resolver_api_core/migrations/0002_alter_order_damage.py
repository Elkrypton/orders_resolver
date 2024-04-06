# Generated by Django 5.0.2 on 2024-04-01 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_resolver_api_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='damage',
            field=models.CharField(choices=[('CUSTOMER_DAMAGE', 'customer damage'), ('VENDOR_DAMAGE', 'vendor damage'), ('RETAIL_DAMAGE', 'retail damage'), ('NONE', None)], default=False, max_length=255, null=True),
        ),
    ]
