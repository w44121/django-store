# Generated by Django 3.2 on 2021-05-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_release_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='release_data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
