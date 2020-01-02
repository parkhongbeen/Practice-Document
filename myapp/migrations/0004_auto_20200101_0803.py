# Generated by Django 2.2.9 on 2020-01-01 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200101_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='성'),
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], help_text='셔츠사이즈이다.', max_length=1, verbose_name='셔츠 사이즈'),
        ),
    ]