# Generated by Django 2.1.5 on 2021-07-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20210727_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('m', 'Erkek'), ('f', 'Kadın'), ('n', 'Belirtmek İstemiyorum'), ('unknown', 'Bilinmiyor')], default='unknown', max_length=10),
        ),
    ]
