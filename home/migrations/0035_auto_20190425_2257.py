# Generated by Django 2.1.5 on 2019-04-25 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_posts_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='post',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
