# Generated by Django 4.1.7 on 2023-09-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_paymentrequest_redeem_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentrequest",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
