# Generated by Django 3.2.9 on 2022-01-15 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_shop_shopowner_delete_shopowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.shop'),
        ),
    ]
