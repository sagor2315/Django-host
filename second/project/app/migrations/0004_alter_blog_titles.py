# Generated by Django 4.1.7 on 2023-03-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titles',
            field=models.CharField(max_length=200, null=True, verbose_name='Titles'),
        ),
    ]