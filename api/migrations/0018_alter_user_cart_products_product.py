# Generated by Django 4.1.3 on 2022-11-11 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_user_cart_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_cart_products',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.products'),
        ),
    ]
