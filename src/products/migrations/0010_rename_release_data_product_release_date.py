# Generated by Django 3.2 on 2021-05-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_release_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='release_data',
            new_name='release_date',
        ),
    ]
