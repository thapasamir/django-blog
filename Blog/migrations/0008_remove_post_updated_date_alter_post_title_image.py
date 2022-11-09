# Generated by Django 4.0.5 on 2022-07-04 11:39

import Blog.fields
import Blog.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='title_image',
            field=Blog.fields.WEBPField(default='posts/home-bg.webp', upload_to=Blog.models.image_folder, validators=[Blog.models.validate_image], verbose_name='Image'),
        ),
    ]
