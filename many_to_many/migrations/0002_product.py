# Generated by Django 2.2.9 on 2020-01-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('similar_products', models.ManyToManyField(related_name='_product_similar_products_+', to='many_to_many.Product')),
            ],
        ),
    ]
