# Generated by Django 4.1.1 on 2023-02-28 11:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_information',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
    ]
