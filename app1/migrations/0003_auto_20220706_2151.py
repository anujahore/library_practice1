# Generated by Django 3.0 on 2022-07-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220706_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(auto_created=True, default=101, primary_key=True, serialize=False),
        ),
    ]