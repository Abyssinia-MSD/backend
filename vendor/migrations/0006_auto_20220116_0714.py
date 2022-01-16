# Generated by Django 3.2.9 on 2022-01-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_productdetail_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='size',
            name='amount',
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='vendor.Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='shope',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='vendor.shop'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='vendor.Size'),
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
    ]
