# Generated by Django 3.0.3 on 2020-03-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0004_auto_20200310_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xyz',
            name='credit',
            field=models.IntegerField(blank=True, max_length=100),
        ),
    ]
