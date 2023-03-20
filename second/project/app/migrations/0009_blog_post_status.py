# Generated by Django 4.1.7 on 2023-03-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
