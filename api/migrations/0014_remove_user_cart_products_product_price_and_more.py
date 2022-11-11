# Generated by Django 4.1.3 on 2022-11-11 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_products_user_cart_products_product_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_cart_products',
            name='product_price',
        ),
        migrations.AddField(
            model_name='user_cart_products',
            name='price',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_price', to='api.products'),
        ),
    ]