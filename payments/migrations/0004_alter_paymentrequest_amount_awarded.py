# Generated by Django 4.1.7 on 2023-09-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0003_paymentrequest_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentrequest",
            name="amount_awarded",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]