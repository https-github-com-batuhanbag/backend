# Generated by Django 2.1.5 on 2021-08-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_auto_20210803_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_subtitle',
            field=models.TextField(max_length=250, verbose_name='Alt Metin'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Başlık'),
        ),
    ]