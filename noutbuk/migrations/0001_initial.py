# Generated by Django 5.0.1 on 2024-01-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noutbuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_n', models.CharField(max_length=20)),
                ('make_n', models.CharField(max_length=20)),
                ('year_n', models.IntegerField(max_length=10)),
                ('color_n', models.CharField(max_length=15)),
                ('price_n', models.DecimalField(decimal_places=2, max_digits=11)),
                ('image_n', models.ImageField(upload_to='media')),
            ],
        ),
    ]
