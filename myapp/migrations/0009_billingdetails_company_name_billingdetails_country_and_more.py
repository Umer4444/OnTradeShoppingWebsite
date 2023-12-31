# Generated by Django 4.2.8 on 2023-12-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_billingdetails_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='order_notes',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='phone',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='street_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='town_city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='zip_code',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
