# Generated by Django 3.2.9 on 2022-01-15 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'womens'), (2, 'mens'), (3, 'kids')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'afar'), (2, 'amhara'), (3, 'benshangul_gumuz'), (4, 'gambela'), (5, 'harari'), (6, 'oromia'), (7, 'snnpr'), (8, 'somalia'), (9, 'tigray')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('location', models.CharField(default=False, max_length=200)),
                ('shopOwner', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('color', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Color', to='vendor.color')),
                ('size', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Size', to='vendor.size')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('category', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='vendor.category')),
                ('product_detail', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductDetail', to='vendor.productdetail')),
                ('type', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='vendor.type')),
            ],
        ),
    ]
