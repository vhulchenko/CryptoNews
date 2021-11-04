# Generated by Django 3.2.6 on 2021-11-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_id', models.PositiveIntegerField(verbose_name='Coin Id')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('symbol', models.CharField(max_length=30, verbose_name='Symbol')),
            ],
        ),
    ]
