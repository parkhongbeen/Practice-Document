# Generated by Django 2.2.9 on 2020-01-02 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_one', '0002_wpsuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpsuser',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_set', to='many_to_one.WPSUser'),
        ),
    ]
