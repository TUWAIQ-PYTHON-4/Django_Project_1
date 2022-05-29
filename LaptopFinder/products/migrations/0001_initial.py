# Generated by Django 4.0.4 on 2022-05-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('type', models.CharField(choices=[('Power User', 'Power User'), ('Everyday use', 'Everyday use'), ('Creative professional', 'Creative professional'), ('Business', 'Business'), ('Gaming', 'Gaming')], max_length=500)),
                ('photo', models.ImageField(blank=True, upload_to='product/photos/')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='brands.brand')),
            ],
        ),
    ]
