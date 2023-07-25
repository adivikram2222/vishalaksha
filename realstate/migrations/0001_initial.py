# Generated by Django 4.2.3 on 2023-07-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_flat_in_property', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('name_of_property', models.CharField(max_length=100)),
                ('number_of_bedrooms', models.IntegerField()),
                ('total_floor', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('furnished_status', models.CharField(choices=[('furnished', 'Furnished'), ('semifurnished', 'Semifurnished'), ('unfurnished', 'Unfurnished')], max_length=100)),
                ('number_of_bathroom', models.IntegerField()),
                ('super_area', models.CharField(max_length=100)),
                ('build_up_area', models.CharField(max_length=100)),
                ('carpet_area', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(choices=[('ready_to_move', 'Ready_to_move'), ('underconstruction', 'Underconstruction'), ('beginning_project', 'Beginning_Project')], max_length=100)),
                ('available_from', models.DateTimeField()),
                ('expected_price', models.IntegerField()),
                ('maintanance_charge_per_month', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('catrgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realstate.category')),
            ],
        ),
    ]
