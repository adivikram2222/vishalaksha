# Generated by Django 4.2.3 on 2023-07-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0003_property_image2_property_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
