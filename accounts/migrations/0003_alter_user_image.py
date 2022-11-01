# Generated by Django 3.2.13 on 2022-11-01 05:03

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
    ]