# Generated by Django 4.2.3 on 2023-07-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0007_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='realestate'),
        ),
    ]
