# Generated by Django 4.2.5 on 2023-11-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_colour_preference_size_remove_product_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
