# Generated by Django 4.1.7 on 2023-03-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_blog_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('G', 'General'), ('S', 'Scrubber')], max_length=1),
        ),
    ]
