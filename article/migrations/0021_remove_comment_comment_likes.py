# Generated by Django 2.1.5 on 2021-08-14 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_comment_comment_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_likes',
        ),
    ]