# Generated by Django 3.0.1 on 2021-11-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spectrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
