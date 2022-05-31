# Generated by Django 4.0.4 on 2022-05-30 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('profile', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='seller/photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='products/photo/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.seller')),
            ],
        ),
    ]
