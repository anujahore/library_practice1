# Generated by Django 3.0 on 2022-07-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]