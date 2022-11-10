# Generated by Django 4.1.3 on 2022-11-10 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_alter_user_cart_products_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_cart_products',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ids', to=settings.AUTH_USER_MODEL),
        ),
    ]
