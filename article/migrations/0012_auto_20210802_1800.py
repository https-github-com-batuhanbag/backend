# Generated by Django 2.1.5 on 2021-08-02 18:00

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20210802_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_subtitle',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name='Makale Alt Başlıgı'),
        ),
    ]
