# Generated by Django 2.1.5 on 2019-02-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190207_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]