# Generated by Django 5.0 on 2023-12-29 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0017_alter_product_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='filter_price',
        ),
        migrations.DeleteModel(
            name='Filter_price',
        ),
    ]