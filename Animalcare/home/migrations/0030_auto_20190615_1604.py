# Generated by Django 2.1.2 on 2019-06-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_home_future_plans_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='future_plans_text',
            field=models.TextField(max_length=22),
        ),
    ]