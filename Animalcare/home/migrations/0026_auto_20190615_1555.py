# Generated by Django 2.1.2 on 2019-06-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20190615_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='about_us_text',
            field=models.TextField(max_length=100),
        ),
    ]