# Generated by Django 2.1.5 on 2021-07-27 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('userprofile', '0003_remove_useraccount_account_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='extra_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialAccount', verbose_name='Extra Data'),
        ),
    ]