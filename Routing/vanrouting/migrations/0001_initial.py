# Generated by Django 4.1.7 on 2023-04-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaninfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=200)),
                ('driver_con', models.CharField(max_length=11)),
                ('van_no', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=200)),
                ('current', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
