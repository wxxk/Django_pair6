# Generated by Django 3.2.13 on 2022-11-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supertype', models.TextField()),
                ('types', models.TextField(null=True)),
                ('name', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='community',
            name='like_user',
        ),
        migrations.RemoveField(
            model_name='community',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Community',
        ),
    ]
