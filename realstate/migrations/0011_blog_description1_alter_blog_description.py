# Generated by Django 4.2.3 on 2023-07-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0010_remove_blog_description1_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
