# Generated by Django 4.2.8 on 2023-12-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Baby', 'Baby'), ('DIY & Tools', 'DIY & Tools'), ('Grocery', 'Grocery'), ('Health & Beauty', 'Health & Beauty'), ('Home & Kitchen', 'Home & Kitchen'), ('Office Products', 'Office Products'), ('Pet Supplies', 'Pet Supplies'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Toys', 'Toys')], max_length=200, null=True),
        ),
    ]