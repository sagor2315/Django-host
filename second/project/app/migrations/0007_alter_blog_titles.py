# Generated by Django 4.1.7 on 2023-03-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_blog_category_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titles',
            field=models.CharField(help_text='Enter your title here', max_length=200, null=True, verbose_name='Title'),
        ),
    ]
