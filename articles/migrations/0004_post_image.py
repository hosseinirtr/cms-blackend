# Generated by Django 4.2.6 on 2023-11-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_post_is_fa_post_slug_tag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_images/'),
        ),
    ]