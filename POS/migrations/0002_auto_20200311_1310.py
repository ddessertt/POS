# Generated by Django 3.0.4 on 2020-03-11 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Type',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='POS.Type'),
        ),
    ]