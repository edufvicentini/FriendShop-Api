# Generated by Django 4.1.3 on 2022-11-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_products_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_url',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user_cart_products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
